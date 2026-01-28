"""
Chat 앱 URL 설정
- 이 앱에서 사용할 URL 패턴을 정의
- 폼 방식으로 단순하게 구성
"""

from django.urls import path
from . import views

# 앱 이름 설정 (템플릿에서 {% url 'chat:index' %} 형태로 사용)
app_name = 'chat'

urlpatterns = [
    # 메인 페이지 (채팅 화면) - GET/POST 모두 처리
    path('', views.index, name='index'),
]
