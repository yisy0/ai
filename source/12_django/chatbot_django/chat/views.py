"""
Chat 앱 뷰
- 사용자 요청을 처리하고 응답을 반환하는 함수들
- AJAX 없이 일반 폼 방식 사용
"""

from django.shortcuts import render, redirect
from .ai_llm import ask_with_reference_rerank
# Create your views here.
def index(request):
  """
  메인 페이지 - 채팅 화면을 보여주고 질문도 처리하는 함수
  - GET 요청: 채팅 화면만 보여줌
  - POST 요청: 질문을 받아서 AI 답변 생성 후 다시 화면 보여줌
  세션에 채팅 기록이 없으면 빈 리스트로 초기화
  """
  if 'chat_history' not in request.session:
    request.session['chat_history'] = []
  # POST 요청이면 질문 처리
  if request.method == 'POST':
    # 폼에서 질문 가져오기
    question = request.POST.get('question', '').strip()
    # 질문이 있으면 AI 답변 생성
    if question:
      try:
        # 세션에서 채팅 기록 가져오기
        chat_history = request.session.get('chat_history', [])
        
        # AI 답변 생성 (기존 스트림릿 코드와 동일한 함수 사용)
        answer = ask_with_reference_rerank(
            query=question,
            chat_history=chat_history,
            k=15,
            top_k=4
        )
        
        # 채팅 기록에 추가 (사용자 질문 + AI 답변)
        chat_history.append({'role': 'user', 'content': question})
        chat_history.append({'role': 'ai', 'content': answer})
        
        # 세션에 저장
        request.session['chat_history'] = chat_history
        request.session.modified = True
          
      except Exception as e:
        # 에러 발생시 에러 메시지를 채팅 기록에 추가
        chat_history = request.session.get('chat_history', [])
        chat_history.append({'role': 'user', 'content': question})
        chat_history.append({'role': 'ai', 'content': f'❌ 오류가 발생했습니다: {str(e)}'})
        request.session['chat_history'] = chat_history
        request.session.modified = True
    
      # POST 처리 후 리다이렉트 (중복 제출 방지 GET방식으로 요청되는 효과나서 새로고침시 비용발생 X)
      return redirect('chat:index')

    # GET 요청이면 채팅 화면 렌더링
  return render(request, 'chat/index.html', {
        'messages': request.session['chat_history']
  })  