from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wordinput(request):
  return render(request, "wordcnt/wordinput.html")

def about(request):
  return render(request, "wordcnt/about.html")

def result(request):
  print(request.GET)
  return HttpResponse(request.GET.items())