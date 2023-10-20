[Environment Setup Instructions]()

 

1     Table of Contents

[**2      INTRODUCTION**](#_Toc148637392)

[**3      STEPS TO COMPLETE**](#_Toc148637393)

[3.1        Accept the IBM Cloud Invitation](#_Toc148637394)

[3.2        Obtain your IBM Cloud API key](#_Toc148637395)

[3.3        Connect to your watsonx.ai instance.](#_Toc148637396)

[3.4        Locate the Watsonx.ai Project Id.](#_Toc148637397)

[3.5        Associate your project with a WML instance (optional)](#_Toc148637398)

[3.6        Clone the workshop Git repo](#_Toc148637399)

[3.7        Install/Update (optional – only for Mac Users)](#_Toc148637400)

[3.8        Install Visual Studio Code (VS Code)](#_Toc148637401)

[3.9        Update credentials in .env file](#_Toc148637402)

[3.10      Create a virtual python environment and install all required libraries.](#_Toc148637403)

[3.11      Ensure you have access to all the IBM Cloud services.](#_Toc148637404)

 

 


# [2       Introduction]()

Complete the steps in this guide to ensure your desktop environment has all the required tools/libraries installed and ensure you have the necessary IBM Cloud access.

 


# [3       Steps to Complete]()

 


## [3.1       Accept the IBM Cloud Invitation]()

Accept the invitation from the IBM Cloud: 2719271-IBM PoC-Watsonx Incubation Program

 

 

![A screenshot of a phone

Description automatically generated](file:////Users/nijesh/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image001.png)


###  

## [3.2       Obtain your IBM Cloud API key]()

You will need your IBM Cloud API key for this lab. If you have an existing API key please us it or follow [these instructions](https://cloud.ibm.com/docs/account?topic=account-userapikey\&interface=ui#create_user_key) to generate a new one in the [IBM cloud](https://cloud.ibm.com/). You will need this API key for next steps.

 


## [3.3       Connect to your watsonx.ai instance.]()

Ensure that you can log into to [watsonx.ai](https://dataplatform.cloud.ibm.com/wx/).

 


## [3.4       Locate the Watsonx.ai Project Id.]()

Ensure you are logged into to [watsonx.ai](https://dataplatform.cloud.ibm.com/wx/).

Select the project under your organization name.

Select the "Manage" tab from your Project's main page.

You will see your Project ID under the "General" tab as shown below.

 

![A screenshot of a computer

Description automatically generated](file:////Users/nijesh/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.png)

 

 

 


## 3.5        [Associate your project with a WML instance (optional)]()

A watsonx.ai project must always be associated with an instance of Watson Machine Learning (WML) before you can use the Prompt Lab or interact with the WML Python SDK.

 

As you are in an instructor-led workshop and the project was created for you, then no further action is required (i.e., an instance of WML should already be associated with the project)

 

If the WML instance is not associated for some reason complete the following steps :

 

1.     Within your newly created watsonx.ai project, click the Manage tab

2.     Select Services & integrations from the side navigation menu

3.     Select the IBM Services tab

4.     Select Associate service +

5.     Choose a WML instance and select Associate

 

 

![A screenshot of a computer

Description automatically generated](file:////Users/nijesh/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image003.png)

![A screenshot of a computer

Description automatically generated](file:////Users/nijesh/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.png)

 


## [3.6       Clone the workshop Git repo]()

 

If you're a Github pro then you can directly clone this [watsonx.ai workshop repo](https://github.com/knijesh/GenAI_Incubation_watsonx/tree/main).

 

Otherwise, we recommend downloading and installing the [Github Desktop](https://desktop.github.com/) and then [cloning this watsonx.ai workshop repo](https://github.com/knijesh/GenAI_Incubation_watsonx/tree/main). Here are instructions on [how to clone a repository using Github Desktop](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop).

 


## [3.7       Install/Update (optional – only for Mac Users)]()

 

Xcode is a collection of developer tools that we will need in this. Access the App Store and search for "xcode." Click the "Get" button or the Cloud icon to install the latest version.

 

![A screenshot of a computer

Description automatically generated](file:////Users/nijesh/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image005.png)

 


## [3.8       Install Visual Studio Code (VS Code)]()

We recommend installing VS Code for this workshop so we are on a common platform for this workshop.

 


## [3.9       Update credentials in .env file]()

 

Python provides support for .env files through a library called dotenv that we will use in this workshop to pass the credentials.

Create a new file in lab 0, and name the file ".env". If you have created the file, but are having trouble viewing it, [learn how to view hidden files on a Mac](https://www.macworld.com/article/671158/how-to-show-hidden-files-on-a-mac.html) or [how to view hidden files on Windows](https://support.microsoft.com/en-us/windows/view-hidden-files-and-folders-in-windows-97fbc472-c603-9d90-91d0-1166d1d9f4b5).

 

![Text Box: API\_KEY=\<your-ibm-cloud-api-key>
IBM\_CLOUD\_URL=https://us-south.ml.cloud.ibm.com
PROJECT\_ID=\<your-project-id>
](file:////Users/nijesh/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image006.png)Open the .env file, add the following content:

 

Use the IBM\_CLOUD\_URL given above. The API\_KEY and PROJECT\_ID need to be filled in by you.

 

1\. Add your IBM Cloud API key from Step 1.2.2 in API\_KEY

2\. Add your project ID from Step 1.2.4 in PROJECT\_ID

 

Save your changes and close the file.

 


## [3.10   Create a virtual python environment and install all required libraries.]()

 

Install all the python libraries using this [requirements\_venv.txt](https://github.com/knijesh/GenAI_Incubation_watsonx/blob/main/lab-0-laptop-environment-setup/requirements_venv.txt).

 

You can use your favourite python package manager and create a virtual environment called genai

and install all the python using this [requirements\_venv.txt](https://github.com/knijesh/GenAI_Incubation_watsonx/blob/main/lab-0-laptop-environment-setup/requirements_venv.txt).

 

Optionally, if you want to use a virtual environment using \`venv\`, follow the steps below.

 

1.     Upgrade to Python v3.11 to avoid any conflicts: Minimum python version needed for our workshop is 3.11. Upgrade your python version to Python 3.11

 

2.     Create your Python virtual environment:

 

a.     Create a folder \<my-folder>

b.     ![Text Box: cd \<directory to store your Python environment>
python -m venv genai
](file:////Users/nijesh/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image007.png)Open a terminal/console window and enter the commands below to create a Python environment called \`genai\`.

c.     Download [requirements\_venv.txt](https://github.com/knijesh/GenAI_Incubation_watsonx/blob/main/lab-0-laptop-environment-setup/requirements_venv.txt)

d.     Move the [requirements\_venv.txt](https://github.com/knijesh/GenAI_Incubation_watsonx/blob/main/lab-0-laptop-environment-setup/requirements_venv.txt) file to the folder \<my-folder>

e.     ![Text Box: source genai/bin/activate
python -m pip install -r requirements\_venv.txt
](file:////Users/nijesh/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image008.png)Activate your Python virtual environment with these commands:

f.      Validate that the start of the prompt line in your terminal/console window changed to genai.

![](file:////Users/nijesh/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image009.png)

 


## [3.11   Ensure you have access to all the IBM Cloud services.]()

 

Login in to ibm cloud account IBM Cloud: 2719271-IBM PoC-Watsonx Incubation Program. Ensure you can see the following services for

1.     Watson Assistant

2.     Watson Discovery

3.     Watson Studio

4.     Watson Machine Learning.

 

![A screenshot of a computer

Description automatically generated](file:////Users/nijesh/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.png)
