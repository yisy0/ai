from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def index(request:HttpRequest) -> HttpResponse:
  context = {"msg":"WordCount Welcome Page",
            "greeting":"Hello, Django(장고)"}
  return render(request=request,
                template_name="home/index.html",
                context=context)
def test(request:HttpRequest) -> HttpResponse:
  return HttpResponse("""<h1>TEST PAGE</h1>
                      
                      """)