# student 앱 아래의 urls.py
# student/          - name="student:list"
# student/get/1     - name="student:get"
# student/delete/1  - name="student:delete"
from django.urls import path, register_converter
from . import views
from .converters import MyConverter
register_converter(MyConverter, "ddd")
app_name = "student"
urlpatterns = [
  path("", views.list, name="list"),
  path("get/<ddd:id>", views.get, name="get"),
  path("delete/<ddd:id>", views.delete, name="delete"),
]