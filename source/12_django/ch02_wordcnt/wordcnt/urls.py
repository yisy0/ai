# wordcnt패키지 안의 urls 모듈
# wordcnt/         : name=wordcnt:wordinput
# wordcnt/about/   : name=wordcnt:abount
# wordcnt/result/  : name=wordcnt:result
from django.urls import path
from wordcnt.views import wordinput, about, result
app_name = "wordcnt"
urlpatterns = [
  path("", wordinput, name="wordinput"), # /wordcnt/ 단어입력 받는 페이지
  path("about/", about, name="about"), # /wordcnt/about/ 도움말
  path("result/", result, name="result"), # /wordcnt/result/ 단어입력결과
]
