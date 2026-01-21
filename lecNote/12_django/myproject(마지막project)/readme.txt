python -m pip install --upgrade pip
pip install django<4.0 python-decouple
pip install django<4.0 python-dotenv
pip install django-extensions : shell_plus 사용 용도 => 앱(django_extensions)등록
장고 프로젝트 생성 : django-admin startproject 프로젝트명 .
==> pip install -r requirements.txt

# from dotenv import load_dotenv
# load_dotenv()
import os
# SECRET_KEY = os.getenv("SECRET_KEY", 'abc')
from decouple import config
SECRET_KEY = config("SECRET_KEY", 'abc')

python manage.py startapp blog


1. settings.py에 앱추가
	'django_extensions', # 추가 앱등록(django 5.2부터는 shell로도 model 자동 import)
	'blog', # 앱등록
    


2. TEMPLATES = [
'DIRS': [
          os.path.join(BASE_DIR, 'myproject', 'templates'),
        ],
]추가

3. STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myproject', 'static'),
]추가

3. base.html과 footer.html, header.html외 static 옮기기


4. JsonResponse 구현
url.py에 path('', views.index),추가
views.py에 아래 함수 추가
 def index(request):
  return JsonResponse(
    {'name':'홍길동', 'age':29}, 
    json_dumps_params={'ensure_ascii': False}
  )추가

5. model 추가

class Post(models.Model): # 테이블명 : blog_post
  # id = models.AutoField(primary_key=True) PK가 없을 경우 자동 생성
  title = models.CharField(verbose_name="제목", max_length=100, null=False, blank=False,
                          help_text="포스팅 제목을 입력해 주세요. 최대 100자 내외")# 최대 길이 반드시 지정 VARCHAR 타입
  content = models.TextField(verbose_name="본문", blank=False) # 최대 길이 제한이 없음 CLOB, TEXT 타입
  create_at = models.DateField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)


admin.site.register(Post)admin에 추가

클래스 생성 -> 테이블 생성
python manage.py makemigrations
python manage.py migrate



View
매개변수(인자) :  요청정보 HttpRequest(request)
리턴값 : 응답정보 HttpResponse
		1) 직접 data
		2) Template => render(request, 탬플릿페이지, context)
		3) subclass (ex) JsonResponse..

Model
클래스 생성 -> 테이블 생성
python manage.py makemigrations
python manage.py migrate

모델명.ojbects.all()
모델명.ojbects.get(pk=값) ; primary key에 해당하는 인스턴스 추출
get_object_or_404(모델명, pk=값)