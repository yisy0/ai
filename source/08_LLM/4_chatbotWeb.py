import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
def main():
  load_dotenv()
  st.set_page_config(page_title="비추 쳇봇")
  # st.text(os.getenv('OPENAI_API_KEY'))
  st.title("비추 쳇봇")
  # 대화 이력을 초기화
  if 'messages' not in st.session_state:
    st.session_state.messages = [
      {'role':"system", "content":"당신은 유능한 AI 상담원입니다"},
      {'role':"user", "content":"2002년 월드컵 성적은?"},
      {'role':"assistant", "content":"4강"},
    ]
  # 대화 이력 표시(system 메세지는 제외)
  for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])
if __name__=="__main__":
  main()