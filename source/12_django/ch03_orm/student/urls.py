# student 앱 아래의 urls.py
# student/          - name="student:list"
# student/get/1     - name="student:get"
# student/delete/1  - name="student:delete"
from django.urls import path, register_converter
from . import views
app_name = "student"
urlpatterns = [
  path("", views.list, name="list"),
]