from django.shortcuts import render
from .models import Book
# 1. form없이 구현 2.form객체생성후
def book_list(request):
  return render(request, "book/book_list.html", {"book_list":Book.objects.all()})
def book_new(request):
  pass
def book_edit(request, pk):
  pass
def book_delete(request, pk):
  pass