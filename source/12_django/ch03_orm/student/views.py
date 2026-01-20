from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from student.models import Student
# Create your views here.
def list(request):
  students = Student.objects.all() # select * from student_student
  #return HttpResponse(students)
  return render(request, "student/list.html", {"students":students})

def get(request, id:int):
  # student = Student.objects.get(pk=id)
  student = get_object_or_404(Student, pk=id) # 없는 id면 DoesNotExist 예외
  return render(request, "student/get.html", {"student":student})