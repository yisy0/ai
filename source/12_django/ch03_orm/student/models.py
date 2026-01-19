from django.db import models

# models.Model로 부터 상속받은 클래스는 DB 테이블(테이블명 : student_student)
# 클래스를 이용한 객체 변수(인스턴스)는 테이블내의 row(레코드)
class Student(models.Model):
  id = models.AutoField(primary_key=True) # 테이블안의 컬럼
  name = models.CharField(max_length=100, unique=True)
  major = models.CharField(max_length=100, null=True, blank=True)
  age = models.IntegerField(default=20)
  grade = models.IntegerField(default=1)
  def __str__(self):
    return "{}.{}님({}, {}학년 {}살)".format(self.id,
                                        self.name,
                                        self.major,
                                        self.grade,
                                        self.age)