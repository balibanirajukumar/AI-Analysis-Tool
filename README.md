****Gen AI Analysis using using streamlit and langchain ****

Requirements
1. An apiKey for the OPNAI
2. Create a virtual env and install the dependencies
   Python3 -m venv .venv
   source .venv/bin/activate

3. Install the dependencies
  pip install streamlit streamlit-authenticator pyyaml langchain pandas
  pip install langchain[openai] langchain[community]

How to run the code:
Clone the repository and move on the new folder AI-analysis-Tool
create .env file and add below information
  OPENAI_API_KEY="your-openai-api-key"
  CHAT_GPT_MODEL="gpt-3.5-turbo" 
streamlit run chatbot_streamlit.py
Upload the data file in csv format
Enter the prompt..!
Enjoy!
