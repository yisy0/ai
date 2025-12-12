# ctrl+shift+p => 인터프리터선택(llm)  
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import time
import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
import streamlit as st
def main():
  load_dotenv()
  st.title("고객 지원 쳇봇")
  # st.text(os.getenv("OPENAI_API_KEY"))
  # client 생성
  client = OpenAI()
  # assistant와 thread 초기화(각각 id를 session에 추가)
  if 'assistant_id' not in st.session_state:
    assistant = client.beta.assistants.create(
      name="CustomerCSBoy",
      instructions="당신은 고객 지원 쳇봇입니다. 사용자 문의에 간략히 대답해 주세요",
      model= "gpt-4o-mini"
    )
    st.session_state.assistant_id = assistant.id
  if "thread_id" not in st.session_state:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id
  # 대화 이력 초기화
  if "messages" not in st.session_state:
    st.session_state.messages = []
  # 대화 이력 표시
  for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

  # 사용자 입력 받기
  if prompt := st.chat_input("메세지를 입력하세요"):
    prompt = prompt.strip()
    # 사용자 메세지를 session 추가, 화면 출력
    st.session_state.messages.append({"role":"user", "content":prompt})
    st.chat_message("user").write(prompt)
    # 사용자 메세지를 thread에 추가
    client.beta.threads.messages.create(
      thread_id = st.session_state.thread_id,
      role = "user",
      content = prompt
    )
    # 실행(답변 요청) - 과금
    client.beta.threads.runs.create_and_poll(
      thread_id = st.session_state.thread_id
    )
    # 최신 답변 가져오기
    reply = "가상 답변"
    st.chat_message("assistant").write(reply)
if __name__=="__main__":
  main()