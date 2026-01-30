from django.shortcuts import render
from django.contrib import messages
from myproject import settings
import os
# Create your views here.
def upload_file(request):
  if request.method == 'POST':
    # 파일첨부 처리
    pass
  else:
    return render(request, "filetest/fileupload.html")

def predict(request):
  pass