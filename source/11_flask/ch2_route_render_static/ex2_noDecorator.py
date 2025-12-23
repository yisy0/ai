# 데코레이터(@) : 대상 함수를 감싸 함수의 앞뒤에 부가적인 구문을 추가 반복 작업
def check(func):
  def wrapper():
    print(func.__name__, '함수 전처리')
    func()
    print(func.__name__, '함수 후처리')
  return wrapper

def hello():
  print('Hello')
def world():
  print('world')

if __name__=="__main__":
  wrapper_hello = check(hello)
  wrapper_hello()
  wrapper_world = check(world)
  wrapper_world()