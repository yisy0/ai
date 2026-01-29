from django.urls import path
from . import views
# 기사목록 /article/          article:list
# 기사추가 /article/new/      article:new
# 기사상세 /article/1/detail  article:detail
# 기사수정 /article/1/edit/   article:edit
# 기사삭제 /article/1/delete/ article:delete
# v2. 검색기능 O, 파일첨부
from .views import ArticleListView, ArticleCreateView
app_name = "article"
urlpatterns = [
  path("", ArticleListView.as_view(), name="list"),
  path("new/", ArticleCreateView.as_view(), name="new"),
  path("<int:pk>/detail", views.article_detail, name="detail"),
  path("<int:pk>/edit/", views.article_edit, name="edit"),
  path("<int:pk>/delete", views.article_delete, name="delete")
]