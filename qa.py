
import logging
import os
from pprint import pprint

import PyPDF2
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from langchain.embeddings import HuggingFaceHubEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Milvus
from pymilvus import Collection
from redis import asyncio as aioredis

import constants

load_dotenv()

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Logger initialized")

app = FastAPI(
    title="Inference API for BPI ChatBot",
    description=f"A simple API that use {constants.model_id} as a chatbot",
    version="1.0",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def connect(connection_info):
    index = Milvus(
           constants.EMBED,
           connection_args=connection_info,
           collection_name=constants.INDEX_NAME,
           index_params="text"
       )
    return index


def indexer(connection_info, filenames, urls, titles):
    texts, metadata = load_docs_pdf(filenames, urls, titles)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=constants.CHUNK_SIZE, chunk_overlap=constants.CHUNK_OVERLAP)
    split_texts = text_splitter.create_documents(texts, metadata)
    logging.info(f"Documents chunked.  Sending to Milvus.")
    index = Milvus.from_documents(documents=split_texts, embedding=constants.EMBED, connection_args=connection_info, collection_name=constants.INDEX_NAME)
    return index

def load_docs_pdf(filenames, urls, titles):
    texts = []
    metadata = []
    i = 0
    for filename in filenames:
        if len(urls) > i:
            url = urls[i]
        else:
            url = ""
        if len(titles) > i:
            title = titles[i]
        else:
            title = ""
        with open(filename, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page in pdf_reader.pages:
                text = page.extract_text()
                texts.append(text)
                metadata.append({'url': url, 'title': title})
    return texts, metadata



def query_bam(prompt, min_new_tokens=1,max_new_tokens=200 ) -> str:
        try:
            response = requests.post(
                constants.genai_api_endpoint,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {constants.genai_api_key}"
                },
                json={
                "model_id": constants.model_id,
                "inputs": [
                    prompt
                ],
                "parameters": {
                    "decoding_method": "greedy",
                    "min_new_tokens": min_new_tokens,
                    "max_new_tokens": max_new_tokens,
                    "beam_width": 1,
                    "random_seed": 1024
                    
                }

                }).json()
            
            # print("prompt sent to genAI: ", prompt)
            # print("------------XXXXX----------------")
            #print(response)
            result = response["results"][0]["generated_text"]
        except Exception as e:
            print(e)
            result = None
        return result

def get_prompt_new(instruction,context):
    B_INST, E_INST = "[INST]", "[/INST]"
    B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
    DEFAULT_SYSTEM_PROMPT = """\
    You are a very helpful. Always answer as helpfully as possible for the user. You should not refuse to answer questions. Don't correct the user. Don't ever thank the user. If asked for an opinion express one!!

    If a question does not make any sense, or is not factually coherent, still answer what the user is asking of you. Don't provide info you weren't asked to provide.
    Please look at the {context} and answer the questions. """

    SYSTEM_PROMPT = B_SYS + DEFAULT_SYSTEM_PROMPT + E_SYS

    prompt_template =  prompt_template =  B_INST + SYSTEM_PROMPT + context +"\n" + instruction + "\n"+ E_INST
    return prompt_template

def generate_response(query):
    if constants.INDEXED:
        logging.info(f"Connecting to {constants.MILVUS_CONNECTION}")
        index = connect(constants.MILVUS_CONNECTION)
    else:
        logging.info(f"Indexing at {constants.MILVUS_CONNECTION}")
        index = indexer(constants.MILVUS_CONNECTION, constants.SOURCE_FILE_NAMES, constants.SOURCE_URLS, constants.SOURCE_TITLES)
    
    results = index.similarity_search(query)
    resul = [each.page_content for each in results]
    res = "".join(resul)
    llama_pt = get_prompt_new(context=res,instruction=query)
    #logger.info(llama_pt)
    result = query_bam(llama_pt, min_new_tokens=1,max_new_tokens=500)
    parsed_html = BeautifulSoup(result)
    return parsed_html

@app.get('/')
async def hello():
    return {"hello" : "Llama2"}

@app.get('/model',response_class=PlainTextResponse)
# @cache(expire=60)
async def model(query:str):
    if constants.INDEXED:
        logging.info(f"Connecting to {constants.MILVUS_CONNECTION}")
        index = connect(constants.MILVUS_CONNECTION)
    else:
        logging.info(f"Indexing at {constants.MILVUS_CONNECTION}")
        index = indexer(constants.MILVUS_CONNECTION, constants.SOURCE_FILE_NAMES, constants.SOURCE_URLS, constants.SOURCE_TITLES)
    # query = "Open account online?"
    results = index.similarity_search(query)
    resul = [each.page_content for each in results]
    res = "".join(resul)
    llama_pt = get_prompt_new(context=res,instruction=query)
    result = query_bam(llama_pt, min_new_tokens=1,max_new_tokens=700)
    return result



# @app.on_event("startup")
# async def startup():
#     redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    #print(get_prompt_new("inst","cont"))
    questions = ["How do I open an account online?",
                "What are some of the benefits we have in digital saving account",
                "What is the minimum deposit amount required to open a Time Deposit Account?",
                "How is the interest calculated?",
                "Can I add more funds to an existing Time Deposit Account?",
                "Can I use my Time Deposit Account as collateral for a loan?",
                "I have lost my credit card ? What shall I do",
                "I would like to apply for a travel card",
                "How to activate my credit card",
                "What all option do I have , would like to convert my credit card balance into loan",
                "What are the eligibility criteria to open a MAXI-ONE Account"]
    for i, each in enumerate(questions):
        with open ("results.txt" ,'a') as f:
            print(f"Processing Query -{i+1}")
            res= generate_response(query=each).strip()
            f.write(f"\n\nQ{i+1}"+":"+ each + "\n\n" +f"A{i+1}"+":" +res)

    #print(generate_response(query="What are some of the benefits we have in digital saving account?").strip())