from django.urls import path
from . import views
# file/ 첨부받음
# file/predict
app_name = "file"
urlpatterns = [
  path("", views.upload_file, name="upload_file"),
  path("predict/", views.predict, name="predict")
]