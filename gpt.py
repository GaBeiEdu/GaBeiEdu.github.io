# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token

import argparse
import json
from argparse import RawTextHelpFormatter
import requests
from typing import Optional
from dotenv import load_dotenv
import warnings
import os
import streamlit as st

load_dotenv()


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "cd4274d0-171f-4ad2-bde6-6e2a20c4bc16"
FLOW_ID = "14616e1c-8409-4986-9f16-e1c774b203c9"
APPLICATION_TOKEN = os.environ.get("GPT_TOKEN")
ENDPOINT = "GabeiEducation" # You can set a specific endpoint name in the flow settings

# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}

def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()



result = run_flow("who are you")



print(result)

# def main():
#     st.title("Chat Interface")
    
#     message = st.text_area("Message", placeholder="Ask something...")
    
#     if st.button("Run Flow"):
#         if not message.strip():
#             st.error("Please enter a message")
#             return
    
#         try:
#             with st.spinner("Running flow..."):
#                 response = run_flow(message)
            
#             response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
#             st.markdown(response)
#         except Exception as e:
#             st.error(str(e))

# if __name__ == "__main__":
#     main()