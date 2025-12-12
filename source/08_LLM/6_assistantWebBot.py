# ctrl+shift+p => 인터프리터선택(llm)  
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import time
import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
import streamlit as st