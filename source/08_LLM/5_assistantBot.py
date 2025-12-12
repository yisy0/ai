# ctrl+shift+p => 인터프리터선택(llm)  
# assistant chatbot
# 1. 어시스턴트 생성 (id확보)
# 2. 스레드 생성(id확보) - 새대화 시작하고 지금부터 대화 history 저장
# while True:
    # 3. 스레드에 사용자 질문 메세지 추가
    # 4. run 실행(어시스턴트가 메세지를 읽고 응답 - 과금)
    # 5. 응답 메세지를 스레드에서 추출하여 출력
# 6. 대화 이력 history.txt로 파일 저장
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import time
import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
# client 생성
load_dotenv()
client = OpenAI()
# 1. assistant 생성
assistant_cs = client.beta.assistants.create(
    name="CustomerQnABot",
    instructions='당신은 고객 지원 쳇봇입니다. 사용자 문의에 대해 간략히 답변해 주세요',
    model = 'gpt-4o-mini'
)
# 2. thread 생성 : 대화 시작
thread_cs = client.beta.threads.create()
print("어서오세요(exit를 입력하시면 종료됩니다)")
while True:
    user_input = input("User :").strip()
    if user_input.lower() in ['exit', '종료']:
        print("이용해 주셔서 감사합니다. 다음에 뵙겠습니다.")
        break
    if user_input == "":
        continue
    # 3. 스레드에 사용자 질문 메세지 추가
    client.beta.threads.messages.create(
        thread_id=thread_cs.id,
        role="user",
        content=user_input
    )
    # 4. run 실행(어시스턴트가 메세지를 읽고 응답 - 과금)
    client.beta.threads.runs.create_and_poll(
        thread_id=thread_cs.id,
        assistant_id=assistant_cs.id
    )
    # 5. 응답 메세지를 스레드에서 추출하여 출력
    messages = client.beta.threads.messages.list(thread_id=thread_cs.id)
    reply = messages.data[0].content[0].text.value # 최신답변
    print("Assistant :", reply)

# 6. 대화 이력 data/ch7_history.txt로 파일 저장
print('이상의 대화 이력을 파일에 백업합니다')
sorted_messages = sorted(messages.data, 
                        key=lambda msg : msg.created_at)
with open('data/ch7_history.txt', 'w', encoding='utf-8') as f:
    for msg in sorted_messages:
        # role / content / dateStr
        role = msg.role
        content = msg.content[0].text.value
        dateStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg.created_at))
        # 파일 기록
        row = "{:9}({}) : {}\n".format(role, dateStr, content)
        f.write(row)