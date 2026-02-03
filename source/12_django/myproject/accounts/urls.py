from django.urls import path
from . import views
"""
accounts.urls - 모든앱을 통틀어 하나밖에 없는 기능이라 app_name을 안 만듦
/accounts/signup (회원가입 - signup) 
/accounts/login/ (로그인 - login)
/accounts/profile/ (회원정보보기 - profile)
/accounts/logout/  (로그아웃 - logout)
"""
urlpatterns = [
  path("signup/", views.signup, name="signup"), # 회원가입
  # path("login/", views.login, name="login"), # 로그인
  path("login/", views.custom_login, name="login"),
  path("profile/", views.profile, name="profile"), #회원정보보기
  path("logout/", views.logout, name="logout"), #로그아웃
]