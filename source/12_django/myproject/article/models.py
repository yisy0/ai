from django.db import models
from django.urls import reverse
# Create your models here.
STATUS_CHOICES = (
  ('d','Draft'), #초안
  ('p', 'Published'), #게재
  ('w', 'Withdrawn') # 철회
)
class Article(models.Model): # 테이블명 : article_article