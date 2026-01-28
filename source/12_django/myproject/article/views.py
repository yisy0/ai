from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Article

# Create your views here.
article_list = ListView.as_view(model=Article)
article_new  = lambda req : None
artcle_detail  = lambda req : None
article_edit  = lambda req : None
article_delete  = lambda req : None