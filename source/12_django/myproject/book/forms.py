from django import forms
from .models import Book
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator
def min_length_2_validator(value):
  if len(value) < 2:
    raise forms.ValidationError("2글자 이상 입력하세요")
  
# class BookForm(forms.Form):
#   title = forms.CharField(label="책이름")
#   author = forms.CharField(label="글쓴이", validators=[min_length_2_validator])
#   publisher = forms.CharField(label="출판사", required=False)
#   sales = forms.IntegerField(label="판매가", initial=1000,
#                             validators=[MinValueValidator(0), MaxValueValidator(100000)])
#   def save(self, commit=True):
#     book = Book(**self.cleaned_data) # cleaned_data입력데이터들을 검증 완료 데이터
#     if commit:
#       book.save()
#     return book

class BookModelForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ['title', 'author', 'publisher', 'sales']
    # fields = '__all__'










