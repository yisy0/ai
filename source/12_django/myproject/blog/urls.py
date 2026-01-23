# blog/urls.py
# blog/~ 요청 경로로 요청이 들어왔을 경우 본 모듈
from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
  path("", views.list, name="list"), # /blog 요청 -> blog:list
  path("<int:post_id>/", views.detail, name="detail"), # /blog/2
]