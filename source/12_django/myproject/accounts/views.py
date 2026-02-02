from django.shortcuts import render
# 회원가입
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.conf import global_settings as settings
from django.shortcuts import redirect

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    # print(form.is_valid())
    if form.is_valid():
      profile = form.save()
      # 회원가입 후 로그인 페이지로 가기
      return redirect(settings.LOGIN_URL)
  else:
    #form = UserCreationForm()
    form = SignupForm()
  return render(request, "accounts/signup_form.html", {"form":form})

def login(request):
  pass

def profile(request):
  pass

def logout(request):
  pass