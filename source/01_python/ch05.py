# ch05.py (ch05 모듈) 자동완성핫키 : ctrl+space
# ctrl+ shift + p => select interpreter을 이용해서 인터프리터(base) 선택
# 실행 : cmd 터미널(ctrl+j)에서 python ch05.py
def my_hello(cnt): #cnt번 반복 
    print(__name__)
    for i in range(cnt):
        print('Hello, Python', end='\t')
        print('Hello, World')
if __name__ == '__main__':
    my_hello(2)