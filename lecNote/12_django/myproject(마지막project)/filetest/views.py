from django.shortcuts import render
from myproject import settings
import os
from django.contrib import messages
# Create your views here.
def upload_file(request):
  if request.method=="POST":
    upload_file = request.FILES.get('file')
    print('파일명 :',upload_file, type(upload_file))
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    if upload_file and upload_file.size<MAX_FILE_SIZE: 
      # 10M미만 파일첨부함
      upload_dir = os.path.join(settings.MEDIA_ROOT, 'filetest')
      os.makedirs(upload_dir, exist_ok=True)
      file_path = os.path.join(upload_dir, upload_file.name)
      with open(file_path, 'wb') as f:
        for chunk in upload_file.chunks(): # 큰 파일 업로드시 조금씩 나눠서 저장(기본 64KB씩)
          f.write(chunk)
      return render(request, 'filetest/result.html')
    elif upload_file and upload_file.size>=MAX_FILE_SIZE:
      # 10M이상 파일첨부함
      messages.error(request, f"파일 사이즈({int(upload_file.size/(1024*1024))}M)가 10M를 초과할 수 없습니다")
    else:
      # 파일 첨부 안 함
      messages.info(request, "파일첨부를 하지 않았습니다")
      messages.success(request, "파일첨부를 하지 않았습니다")
      messages.warning(request, "파일첨부를 하지 않았습니다")
  return render(request, "filetest/fileupload.html")
import time
def predict(request):
  time.sleep(3)
  return render(request, "filetest/predict.html", {"answer":"Hello, World!"})