# file/         DB에 저장없이 파일 첨부 받기(name=file:upload_file)
# file/predict/ 예측결과 출력하기           (name=file:predict)
from django.urls import path
from . import views
app_name = "file"
urlpatterns = [
  path("", views.upload_file, name="upload_file"),
  path("predict/", views.predict, name="predict"),
]