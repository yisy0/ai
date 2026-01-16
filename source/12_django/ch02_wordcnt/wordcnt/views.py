from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wordinput(request):
  return render(request, "wordcnt/wordinput.html")

def about(request):
  return render(request, "wordcnt/about.html")

def result(request):
  #print(request.GET)
  # fulltxt = request.GET['fulltxt']
  # fulltxt = request.GET.get('fulltxt', '') # 홍길동 홍길동 아자
  fulltxt = request.POST.get('fulltxt', '')
  strlength = len(fulltxt) # 글자수(10)
  words = fulltxt.split() # space단위로 단어 분리 ['홍길동', '홍길동', '아자']
  words_dic = dict() # 빈딕셔너리 => {'홍길동':2, '아자':1}
  for word in words:
    if word in words_dic.keys():
      words_dic[word] += 1 # {'홍길동':2}
    else:
      words_dic[word] = 1 # {'홍길동':1, '아자':1 }
  #  {'홍길동':2, '아자':1}
  context = {
    'fulltxt':fulltxt,
    'strlength':strlength, # 글자수
    'wordcnt':len(words), # 단어 갯수
    'dict' : words_dic.items() # [('홍길동',2), ('아자',1)]
  }
  # print(words_dic.items())
  return render(request=request,
                template_name="wordcnt/result.html", 
                context=context)