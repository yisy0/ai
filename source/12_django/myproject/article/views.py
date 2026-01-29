from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Article
from django.core.paginator import Paginator
from django.urls import reverse_lazy
# /article : 1페이지   /article?page=3
# def article_list(request):
#   article_list = Article.objects.all()
#   q = request.GET.get('q', '')
#   if q:
#     article_list = article_list.filter(title__icontains = q)
#   paginator = Paginator(article_list, per_page=3)
#   page_number = request.GET.get('page', '1')
#   page_object = paginator.get_page(page_number)
#   return render(request, "article/article_list.html",
#                 {"article_list":page_object,
#                 "page_obj":page_object,
#                 "q":q})
class ArticleListView(ListView):
  model = Article
  paginate_by = 3 # 한페이지당 3개씩 출력
  def get_queryset(self):
    article_list = super().get_queryset()
    q = self.request.GET.get('q', '')
    if q:
      article_list = article_list.filter(title__icontains=q)
    return article_list
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['q'] = self.request.GET.get('q','')
    return context

class ArticleCreateView(CreateView):
  model = Article
  fields="__all__"

from django.utils import timezone
class ArticleDetailView(DetailView):
  model = Article
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['now'] = timezone.now()
    return context

class ArticleUpdateView(UpdateView):
  model = Article
  fields="__all__"

class ArticleDeleteView(DeleteView):
  model=Article
  success_url=reverse_lazy("article:list")