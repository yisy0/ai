from django.db import models
from django.urls import reverse
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
  # photo 추가(파일첨부)
  def __str__(self):
    return f"{self.id}.{self.title}"
  def get_absolute_url(self):
    # return reverse("article:list") # create, update후 url
    return reverse("article:detail", args=[self.id]) # create, update후 url : 해당 기사 상세보기
  class Meta:
    ordering = ['-id'] # id 내림차순 정렬