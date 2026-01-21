from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import global_settings as settings
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.