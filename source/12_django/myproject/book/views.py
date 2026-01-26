from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Book
# 1. form없이 구현 2.form객체생성후(6장) 3.DjangoGenericView 이용 4.GenericView상속(7장)
# def book_list(request):
#   return render(request, "book/book_list.html", {"book_list":Book.objects.all()})
book_list = ListView.as_view(model=Book)

def book_new(request):
  # GET : template 페이지(book/book_form.html)로 응답
  # POST : 파라미터변수받아 유효성 체크
    # 1) success => db에 save() -> book:list로
    # 2) fail => 오류메세지와 함께 입력페이지로 이동 (form 객체 활용)
  if request.method == 'POST':
    # 파라미터 받아 ip까지 입력한 후 db에 저장
    title = request.POST.get('title')
    author = request.POST.get('author')
    publisher = request.POST.get('publisher')
    sales = int(request.POST.get('sales'))
    ip = request.META.get('REMOTE_ADDR', 'localhost')
    book = Book(title=title, author=author, publisher=publisher, sales=sales, ip=ip)
    book.save()
    return red
  elif request.method == 'GET':
    return render(request, "book/book_form.html")



def book_edit(request, pk):
  pass
def book_delete(request, pk):
  pass