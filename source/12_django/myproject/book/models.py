from django.db import models
from django import forms
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
def min_length_2_validator(value):
  if len(value) < 2:
    raise forms.ValidationError("2글자 이상 입력하세요")
def salesCheck(value):
  if not 0 <= value <= 100000:
    raise forms.ValidationError("판매가는 0~10만 사이만 가능합니다")
class Book(models.Model): # book_book 테이블
  title = models.CharField(verbose_name="책이름", max_length=50)
  author = models.CharField(verbose_name="책저자", 
                            max_length=50,
                            validators=[
                              min_length_2_validator,
                              # MinLengthValidator(2, message="")
                            ])
  publisher = models.CharField(verbose_name="출판사",
                              max_length=50,
                              null=True, blank=True)
  sales = models.IntegerField(verbose_name="판매가", default=1000,
                              validators=[])