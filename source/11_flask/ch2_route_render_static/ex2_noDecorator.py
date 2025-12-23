# 데코레이터(@) : 대상 함수를 감싸 함수의 앞뒤에 부가적인 구문을 추가 반복 작업
def hello():
  print(hello.__name__, '함수 전처리')
  print('Hello')
  print(hello.__name__, '함수 후처리')
def world():
  print(world.__name__, '함수 전처리')
  print('world')
  print(world.__name__, '함수 후처리')