from langchain.embeddings import HuggingFaceHubEmbeddings

SOURCE_FILE_NAMES=["data/account.pdf","data/leave.pdf","data/TD.pdf",'data/travel.pdf']


# SOURCE_FILE_NAMES=["/Users/nijesh/Documents/Work/VectorStore_Milvus/THINK/ge-great-supremehealth_ac0423-policy-contract_v1-1-(clean).pdf","/Users/nijesh/Documents/Work/VectorStore_Milvus/THINK/ge-great-supremehealth_nac0423-policy-contract_v1-1-(clean).pdf",
#                    "/Users/nijesh/Documents/Work/VectorStore_Milvus/THINK/ge-great-supremehealth_sp0423-policy-contract_v1-1-(clean).pdf","/Users/nijesh/Documents/Work/VectorStore_Milvus/THINK/income-enhanced-incomeshield-contract_202304 (1).pdf",
#                    "/Users/nijesh/Documents/Work/VectorStore_Milvus/THINK/income-incomeshield-contract-with-schedule-v202304 (1).pdf","/Users/nijesh/Documents/Work/VectorStore_Milvus/THINK/income-standard-incomeshield-plan-contract_v202304.pdf"]


SOURCE_URLS=[]
SOURCE_TITLES=[]
"""WML instance 006cbc80-137c-4057-bb83-c1f96eaf7213 status is not active, current status: Inactive"""

# SOURCES_TOPIC should be a single title that describes all of the sources.  The LLM uses it to decide whether to search those sources.
SOURCES_TOPIC="BPI_llama_70b_v2"

INDEX_NAME="collect_BPI_llama_70b_v2"



# SOURCES_TOPIC="THINK"

# INDEX_NAME="THINK"

EMBED = HuggingFaceHubEmbeddings(repo_id="sentence-transformers/all-MiniLM-L6-v2")

MILVUS_CONNECTION={"host": "128.168.140.66", "port": "19530"}

CHUNK_SIZE=1200
CHUNK_OVERLAP=200
INDEXED = False

# genai_api_endpoint = "https://bam-api.res.ibm.com/v1/generate"
# genai_api_key = "pak-uxBIxk0mVx9PsukFin8OGffM955c4EhmCQIZRiKdNEY"


genai_api_endpoint = "https://workbench-api.res.ibm.com/v1/generate"
genai_api_key = "pak-sBf0GDvBklfrdPO8RuK2CdNLN7UIQ64oC8dqb_cpRew"


# genai_api_endpoint = "https://us-south.ml.cloud.ibm.com/ml/v1-beta/generation/text?version=2023-05-29"
# genai_api_key = "wG7WdV_RkGt1f8gSKstmD4xw_IyagYAbBUouJOjhKegB"



model_id = "meta-llama/llama-2-70b-chat"