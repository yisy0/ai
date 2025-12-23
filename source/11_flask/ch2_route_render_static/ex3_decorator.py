# 데코레이터(@) : 대상 함수를 감싸 함수의 앞뒤에 부가적인 구문을 추가 반복 작업
def check(func):
  def wrapper():
    print(func.__name__, '함수 전처리')
    func()
    print(func.__name__, '함수 후처리')
  return wrapper
@check
def hello():
  print('Hello')

@check
def world():
  print('world')

if __name__=="__main__":
  hello()
  world()