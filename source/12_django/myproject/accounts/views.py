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
      profile = form.save()
      # 회원가입 후 로그인 페이지로 가기
      return redirect(settings.LOGIN_URL) # 회원가입 성공 후 로그인 페이지로 
      # return redirect("/accounts/login")
      # return redirect("login")
  else:
    #form = UserCreationForm()
    form = SignupForm()
  return render(request, "accounts/signup_form.html", {"form":form})

from django.contrib.auth.views import LoginView, LogoutView
login = LoginView.as_view(template_name="accounts/login_form.html") #로그인

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
  