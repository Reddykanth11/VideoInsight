import streamlit as st
import google.generativeai as genai
import os

# This pulls your API Key from the server's hidden settings
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

st.set_page_config(page_title="Gemini AI App")
st.title("🚀 My Live Gemini Project")

user_input = st.text_area("Enter your prompt:", placeholder="Type something here...")

if st.button("Generate Response"):
    if not api_key:
        st.error("API Key is missing! Please add it to Secrets.")
    else:
        model = genai.GenerativeModel('gemini-1.5-flash')
        with st.spinner("Thinking..."):
            response = model.generate_content(user_input)
            st.write(response.text)
