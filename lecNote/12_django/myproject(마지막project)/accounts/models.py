from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User,
          on_delete=models.CASCADE) # User가 삭제될 때, profile은 어떻게 할지?
  phone_number = models.CharField(verbose_name="전화", max_length=20)
  address      = models.CharField(verbose_name="주소", max_length=100)
  def __str__(self):
    return "{}({}-{})".format(self.user.username,
                              self.phone_number,
                              self.address)
  
# 이벤트 처리 : 회원가입 완료(user.save()성공) 후 가입인사를 메일 전송
from django.db.models.signals import post_save
from django.conf.global_settings import AUTH_USER_MODEL
from django.core.mail import send_mail
def on_send_mail(sender, **kwargs):
  if kwargs['created']:
    user = kwargs['instance'].user
    title = user.username + '님 가입을 환경합니다'
    body = user.username + '님 가입 감사합니다'
    bodyhtml = '<h1>{}님 가입 환영합니다</h1><h2>진심진심</h2>'.format(user.username)
    # settings.py 에 stmp 설정이 셋팅
    send_mail(subject=title,
              message=body,
              from_email= 'yisy0703@naver.com',
              recipient_list = [user.email],
              fail_silently=False, # 메일 전송이 안 되었을 경우 아무일도 하지 않음
              html_message=bodyhtml
    )

post_save.connect(on_send_mail, sender=Profile)