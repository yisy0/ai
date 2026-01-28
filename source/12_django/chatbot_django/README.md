# Django 챗봇 프로젝트

Django 기반의 AI 챗봇 웹 애플리케이션입니다.

## 📋 프로젝트 개요

이 프로젝트는 Django 프레임워크를 사용하여 구축된 **소득세법 전문 AI 챗봇** 시스템입니다. 
사용자의 소득세 관련 질문에 대해 RAG(Retrieval-Augmented Generation) 기술을 활용하여 정확하고 상세한 답변을 제공합니다.
세션 기반으로 대화 이력을 관리하며, 웹 인터페이스를 통해 접근할 수 있습니다.

## 🏗️ 프로젝트 구조

```
CHATBOT/
├── .venv/                    # 가상환경
├── chat/                     # 메인 챗봇 앱
│   ├── migrations/          # 데이터베이스 마이그레이션
│   ├── __init__.py
│   ├── admin.py            # Django 관리자 설정
│   ├── ai_functions.py     # AI 관련 함수
│   ├── ai_llm.py          # LLM(Large Language Model) 연동
│   ├── apps.py            # 앱 설정
│   ├── models.py          # 데이터베이스 모델
│   ├── tests.py           # 테스트 코드
│   ├── urls.py            # URL 라우팅
│   └── views.py           # 뷰 로직
├── chatbot/                 # 프로젝트 설정 디렉토리
│   ├── static/
│   │   └── css/
│   │       └── chat.css   # 챗봇 스타일시트
│   ├── templates/
│   │   └── chat/
│   │       └── index.html # 메인 템플릿
│   ├── __init__.py
│   ├── asgi.py           # ASGI 설정
│   ├── settings.py       # Django 설정
│   ├── urls.py           # 메인 URL 설정
│   └── wsgi.py           # WSGI 설정
├── .env                     # 환경 변수 (API 키 등)
├── db.sqlite3              # SQLite 데이터베이스
├── manage.py               # Django 관리 스크립트
└── requirements.txt        # 프로젝트 의존성
```

## 🚀 설치 및 실행 방법

# 1. 가상환경 생성 및 활성화
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# 2. 의존성 패키지 설치
pip install -r requirements.txt

# 3. 환경 변수 설정
# .env 파일을 생성하고 필요한 API 키를 설정하세요

# 4. 데이터베이스 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 5. 개발 서버 실행
python manage.py runserver
```

### 3. 접속

브라우저에서 `http://127.0.0.1:8000/` 또는 `http://localhost:8000/`으로 접속하세요.

## 🔧 주요 기능

- **소득세법 전문 상담**: 소득세법 관련 질문에 대해 정확한 법률 정보 제공
- **RAG 기반 검색**: Reference Reranking을 통한 고품질 답변 생성
  - 벡터 검색으로 관련 문서 15개 검색 (k=15)
  - Reranking으로 상위 4개 선별 (top_k=4)
- **세션 기반 대화 이력**: Django 세션을 활용한 대화 맥락 유지
  - 사용자별 독립적인 대화 이력 관리
  - 새로고침 시에도 대화 내용 유지
  - 브라우저 종료 전까지 세션 유지
- **폼 기반 통신**: AJAX 없이 일반 POST/Redirect/GET 패턴 사용
  - 새로고침 시 중복 요청 방지
  - 안정적인 폼 처리
- **반응형 UI**: 모바일과 데스크톱 모두에서 사용 가능한 인터페이스
- **에러 핸들링**: AI 처리 중 발생하는 오류를 사용자에게 친절하게 안내

## 📦 주요 의존성 패키지

```
pip install Django python-dotenv langchain langchain-openai langchain-core langchain-pinecone openai pinecone-client cohere tiktoken
```

*전체 의존성 목록은 `requirements.txt`를 참조하세요.*


## 🛠️ 개발 가이드

### 세션 기반 대화 이력 관리

이 프로젝트는 Django 세션을 사용하여 대화 이력을 관리합니다:

```python
# views.py에서 세션 사용 예시

# 세션 초기화
if 'chat_history' not in request.session:
    request.session['chat_history'] = []

# 대화 추가
chat_history = request.session.get('chat_history', [])
chat_history.append({'role': 'user', 'content': question})
chat_history.append({'role': 'ai', 'content': answer})

# 세션 저장 (반드시 필요!)
request.session['chat_history'] = chat_history
request.session.modified = True  # 세션 변경 알림
```

**세션 설정 (settings.py)**:
```python
# 세션 엔진 설정
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # DB 기반
# 또는
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 캐시 기반

# 세션 만료 시간 (초)
SESSION_COOKIE_AGE = 3600  # 1시간

# 브라우저 종료시 세션 삭제
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```

### RAG 파라미터 조정

`chat/ai_llm.py`의 `ask_with_reference_rerank` 함수에서 파라미터를 조정할 수 있습니다:

```python
answer = ask_with_reference_rerank(
    query=question,           # 사용자 질문
    chat_history=chat_history,  # 대화 이력
    k=15,                     # 초기 검색할 문서 수 (늘리면 더 많은 문서 검색)
    top_k=4                   # Rerank 후 최종 선택할 문서 수
)
```

- **k 값 증가**: 더 넓은 범위 검색, 처리 시간 증가
- **top_k 값 증가**: 더 많은 컨텍스트 제공, 토큰 사용량 증가

### 새로운 AI 기능 추가

1. `chat/ai_functions.py`에 새로운 함수 추가
2. `chat/ai_llm.py`에서 LLM 연동 로직 구현
3. `chat/views.py`에서 뷰 로직 연결

## 🐛 트러블슈팅

### 세션 관련 오류

**세션이 저장되지 않을 때:**
```python
# views.py에서 세션 수정 후 반드시 추가
request.session.modified = True
```

**세션 테이블이 없다는 오류:**
```bash
# 세션 테이블 생성
python manage.py migrate
```

**세션 초기화가 필요할 때:**
```bash
# Django 셸에서 모든 세션 삭제
python manage.py shell
>>> from django.contrib.sessions.models import Session
>>> Session.objects.all().delete()