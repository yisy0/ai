from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
# Create your views here.
def list(request):
  print("request:user", request.user) # 로그인전 : AnonymousUser객체/로그인후:로그인한 User객체
  post_list = Post.objects.all()
  return render(request, "blog/index.html", {"post_list":post_list, 
                                            # "user":request.user
                                            })
def detail(request, post_id:int):
  post = Post.objects.get(id=post_id)
  return render(request, "blog/detail.html", {"post":post})