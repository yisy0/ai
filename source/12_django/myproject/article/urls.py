from django.urls import path
from . import views
# 기사목록 /article/          article:list
# 기사추가 /article/new/      article:new
# 기사상세 /article/1/detail  article:detail
# 기사수정 /article/1/edit/   article:edit
# 기사삭제 /article/1/delete/ article:delete
# v2. 검색기능 O, 파일첨부
from .views import ArticleListView, ArticleCreateView, ArticleDetailView
from .views import ArticleUpdateView, ArticleDeleteView
app_name = "article"
urlpatterns = [
  path("", ArticleListView.as_view(), name="list"),
  path("new/", ArticleCreateView.as_view(), name="new"),
  path("<int:pk>/detail", ArticleDetailView.as_view(), name="detail"),
  path("<int:pk>/edit/", ArticleUpdateView.as_view() , name="edit"),
  path("<int:pk>/delete", ArticleDeleteView.as_view(), name="delete")
]