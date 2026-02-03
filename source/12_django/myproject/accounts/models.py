from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone_number = models.CharField(verbose_name="전화", max_length=20)
  address      = models.CharField(verbose_name="주소", max_length=100)
  def __str__(self):
    return "{}({}-{})".format(self.user.username, self.phone_number, self.address)
  
# 이벤트처리 : Profile insert 시 가입인사 메일를 전송 => signals(post_save)
from django.db.models.signals import post_save
from django.core.mail import send_mail
from myproject.settings import EMAIL_HOST_USER
def on_send_mail(sender, **kwargs):
  #print(kwargs)
  if kwargs['created']:
    user = kwargs['instance'].user
    if not user.email:
      print("메일 주소가 없어서 메일을 못 보냈습니다")
      return
    subject = user.username + "님 회원가입 환영합니다"
    body = user.username +"님 가입 감사합니다"
    bodyHtml = """<h1>{}님 가입 감사합니다</h1>
    <h2 style="color:red">진심진심</h2>
    <img src="https://cdn.crowdpic.net/detail-thumb/thumb_d_A84C60D08FC6B681D602F41323B42307.png">
    """.format(user.username)
    # settings.py에 smtp 셋팅
    send_mail(
      subject=subject,
      message=body,
      from_email=EMAIL_HOST_USER,
      recipient_list=[user.email],
      fail_silently=False, # 메일 전송이 안 되었을 때, 아무일도 하지 않음
      html_message=bodyHtml
    )
    print("회원 가입후 메일 전송 완료")

post_save.connect(on_send_mail, sender=Profile) # Profile인스턴스 DB save 후 on_send_mail실행