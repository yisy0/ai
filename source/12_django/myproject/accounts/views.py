from django.shortcuts import render
# 회원가입
from django.contrib.auth.forms import UserCreationForm
from django.conf import global_settings as settings

def signup(request):
  if request.method == 'POST':
    pass # 회원가입 처리
  else:
    form = UserCreationForm()
  return render(request, "accounts/signup_form.html", {"form":form})

def login(request):
  pass

def profile(request):
  pass

def logout(request):
  pass