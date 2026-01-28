from django.urls import path
from . import views
# 기사목록 /article/          article:list
# 기사추가 /article/new/      article:new
# 기사상세 /article/1/detail  article:detail
# 기사수정 /article/1/edit/   book:edit
# 기사삭제 /article/1/delete/ book:delete
app_name = "article"
urlpatterns = [
  path("", views.book_list, name="list"),
  path("new/", views.book_new, name="new"),
  path("<int:pk>/edit/", views.book_edit, name="edit"),
  path("<int:pk>/delete", views.book_delete, name="delete"),
]