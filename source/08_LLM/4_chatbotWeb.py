import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
def main():
  load_dotenv()
  st.set_page_config(page_title="비추 쳇봇")
  st.text(os.getenv('OPENAI_API_KEY'))

if __name__=="__main__":
  main()