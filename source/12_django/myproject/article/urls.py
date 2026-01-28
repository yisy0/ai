from django.urls import path
from . import views
# 기사목록 /article/          article:list
# 기사추가 /article/new/      article:new
# 기사상세 /article/1/detail  article:detail
# 기사수정 /article/1/edit/   article:edit
# 기사삭제 /article/1/delete/ article:delete
# v1. 검색기능 X
app_name = "article"
urlpatterns = [
  path("", views.article_list, name="list"),
  path("new/", views.article_new, name="new"),
  path("<int:pk>/detail", views.artcle_detail, name="detail"),
  path("<int:pk>/edit/", views.article_edit, name="edit"),
  path("<int:pk>/delete", views.article_delete, name="delete"),
]