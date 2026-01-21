from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post) # admin 페이지에 Post 테이블 액세스 가능