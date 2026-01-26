from django.urls import path
from . import views
# 책목록 /book/          book:list
# 책추가 /book/new/      book:new
# 책수정 /book/1/edit/   book:edit
# 책삭제 /book/1/delete/ book:delete
app_name = "book"
urlpatterns = [
  path("", views.book_list, name="list"),
  path("new/", views.book_new, name="new"),
  path("<int:pk>/edit/", views.book_edit, name="edit"),
  path("<int:pk>/delete", views.book_delete, name="delete"),
]