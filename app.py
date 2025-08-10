import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "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"}  # Replace with your key

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print("Status code:", response.status_code)       # debug
    print("Response:", response.text)                 # debug
    return response.json()


# Streamlit UI
st.set_page_config(page_title="AI Text Summarizer", page_icon="📝")
st.title("📝 AI Text Summarizer")
st.write("Paste your text below and get a concise summary!")

text_input = st.text_area("Enter your text here...", height=200)

if st.button("Summarize"):
    if text_input.strip():
        with st.spinner("Generating summary..."):
            output = query({"inputs": text_input})
            if isinstance(output, list) and "summary_text" in output[0]:
                st.subheader("Summary:")
                st.write(output[0]['summary_text'])
            else:
                st.error("Error generating summary. Please try again.")
    else:
        st.warning("Please enter some text first!")
