from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Article
from django.core.paginator import Paginator
# /article : 1페이지   /article?page=3

# article_list = ListView.as_view(model=Article, paginate_by=3) # 한페이지에 3행씩
article_new  = lambda req : None
artcle_detail  = lambda req : None
article_edit  = lambda req : None
article_delete  = lambda req : None