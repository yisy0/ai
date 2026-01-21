from django.db import models
import re
from django.forms import ValidationError
from django.utils import timezone
# Create your models here.

class Post(models.Model): #테이블명 : blog_post
  # id = models.AutoField(primary_key=True) PK가 없을 경우 자동 생성
  title = models.CharField(verbose_name="제목", # form의 라벨
                          max_length=100, # 최대 문자 길이 반드시 지정 VARCHAR(100)
                          help_text="기사 제목입니다. 100자 내외로 입력하세요"
                          )
  content = models.TextField("본문") # 최대 문자 길이 제한 없음 CLOB타입, TEXT타입
  create_at = models.DateField(auto_now_add=True) # 등록일 자동 저장
  update_at = models.DateTimeField(auto_now=True) # 등록/수정 날짜와시간 자동 저장
  def __str__(self):
    updated = timezone.localtime(self.update_at).strftime("%Y-%m-%d %H:%M")
    return "제목:{} - {}작성. {}최종수정".format(self.title,
                                        self.create_at,
                                        updated)