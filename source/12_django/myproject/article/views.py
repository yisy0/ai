from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Article
from django.core.paginator import Paginator
from django.urls import reverse_lazy
# /article : 1페이지   /article?page=3
# def article_list(request):
#   article_list = Article.objects.all()
#   paginator = Paginator(article_list, per_page=3)
#   page_number = request.GET.get('page', '1')
#   page_object = paginator.get_page(page_number)
#   return render(request, "article/article_list.html",
#                 {"article_list":page_object,
#                 "page_obj":page_object})
article_list = ListView.as_view(model=Article, paginate_by=3) # 한페이지에 3행씩

article_new  = CreateView.as_view(model=Article, fields="__all__")

article_detail  = DetailView.as_view(model=Article)

article_edit  = UpdateView.as_view(model=Article, fields="__all__")

article_delete  = DeleteView.as_view(model=Article,
                                    success_url=reverse_lazy("article:list"))