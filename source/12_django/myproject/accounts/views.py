from django.shortcuts import render

# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.conf import global_settings as settings
from django.shortcuts import redirect
def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    # print(form.is_valid())
    if form.is_valid():
      profile = form.save() # DB 저장
      # 회원가입 후 로그인 페이지로 가기
      request.session["username"] = profile.user.username # 회원가입한 username을 session추가
      return redirect(settings.LOGIN_URL) # 회원가입 성공 후 로그인 페이지로 
      # return redirect("/accounts/login")
      # return redirect("login")
  else:
    #form = UserCreationForm()
    form = SignupForm()
  return render(request, "accounts/signup_form.html", {"form":form})

from django.contrib.auth.views import LoginView, LogoutView
# login = LoginView.as_view(template_name="accounts/login_form.html") #로그인

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
def custom_login(request):
  initial_username = request.session.get("username")
  if request.method == "POST":
    # 로그인처리
    form = AuthenticationForm(request=request, data=request.POST)
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user) # Django에서 user를 세션에 저장
      # request.session["username"] = username # 세션에 username 저장
      next_url = request.GET.get("next", "profile")
      return redirect(next_url)
    # else:
    #   form.add_error(None, "떼끼") # 로그인 실패시 오류 메세지 추가
  else:
    form = AuthenticationForm(
      request=request, 
      initial={"username":initial_username} # 회원가입후 바로 로그인한 경우 username
    )
    #print(form)
  return render(request, "accounts/login_form.html", {"form":form})

logout = LogoutView.as_view(next_page=settings.LOGIN_URL) # 로그아웃(로그아웃 후에는 로그인)
# 회원정보 보기
from django.contrib.auth.decorators import login_required
from .models import Profile
@login_required
def profile(request):
  profile, created = Profile.objects.get_or_create(
    user = request.user
  )
  print("profile:", profile, "\t created:", created)
  return render(request, "accounts/profile.html",
                {"profile":profile, 
                #"user":request.user,
                "is_new_profile":created})
  