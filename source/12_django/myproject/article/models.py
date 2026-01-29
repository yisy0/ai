from django.db import models
from django.urls import reverse
from django.shortcuts import get_object_or_404
import os
from myproject import settings
# Create your models here.
STATUS_CHOICES = (
  ('d','Draft'), #초안
  ('p', 'Published'), #게재
  ('w', 'Withdrawn') # 철회
)
class Article(models.Model): # 테이블명 : article_article
  title = models.CharField(verbose_name="제목", max_length=100)
  body  = models.TextField(verbose_name="본문")
  status = models.CharField(max_length=1, choices=STATUS_CHOICES)
  # photo 추가(파일첨부) : pip install pillow -> pip freeze > requirements.txt
  # python manage.py makemigrations -> python manage.py migrate
  photo = models.ImageField(verbose_name="사진",
                            blank=True, # _media/ 폴더에 자동 저장
                            upload_to="article/%Y/%m/%d")
  def save(self, *args, **kwargs):
    if self.pk: # 수정 여부(create시 self.pk가 None)
      # db_instance = Article.objects.get(pk=self.pk)
      db_instance = get_object_or_404(Article, pk=self.pk)
      if db_instance.photo and db_instance.photo != self.photo:
        file_path = os.path.join(settings.MEDIA_ROOT, str(db_instance.photo))
        if os.path.exists(file_path): # 파일존재여부
          os.remove(file_path) # 파일 삭제
    super().save(args, kwargs)

  def delete(self, *args, **kwargs):
    if self.photo: # 지울 article의 phone 존재 여부
      file_path = os.path.join(settings.MEDIA_ROOT, str(self.photo))
      print(file_path, '파일도 지우고 DB도 지우고')
      if os.path.exists(file_path):
        os.remove(file_path)
    super().delete(args, kwargs)
  
  def __str__(self):
    return f"{self.id}.{self.title}"
  def get_absolute_url(self):
    # return reverse("article:list") # create, update후 url
    return reverse("article:detail", args=[self.id]) # create, update후 url : 해당 기사 상세보기
  class Meta:
    ordering = ['-id'] # id 내림차순 정렬