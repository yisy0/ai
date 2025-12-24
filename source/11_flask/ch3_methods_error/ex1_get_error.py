# 가상환경 생성방법1 : python -m venv .venv
# 가상환경 생성방법2 : ctrl+shift+p => select interpreter => 가상환경만들기 
#        => .venv로 가상환경만들기 => 인터프리터경로입력 => 찾기(python.exe)
# 가상환경 생성방법2를 사용하면 pip 업그레이드와 가상환경 들어가기까지 포함
# pip install pydantic flask
# pip freeze > requirements.txt
from flask import Flask # 앱 객체(서버)
from flask import render_template # html렌더링
from flask import request # get/post방식으로 파라미터 데이터 받기
from flask import abort # 강제 예외발생

app = Flask(__name__)

@app.route('/user/<name>') # /user/hong
def viewFunction_handlerFunction(name):
  