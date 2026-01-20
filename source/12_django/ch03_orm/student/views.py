from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student
# Create your views here.
def list(request):
  students = Student.objects.all() # select * from student_student
  #return HttpResponse(students)
  return render(request, "student/list.html", {"students":students})