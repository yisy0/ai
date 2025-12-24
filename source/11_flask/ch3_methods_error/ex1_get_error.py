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

@app.route('/user/<name>') # /user/hong (동적라우팅 : update, delete할 때)
def viewFunction_handlerFunction(name):
  return f"<h1>{name}님 환영합니다</h1>"
@app.route('/user')        # /user?name=hong (정적라우팅 : read/create할 때)
def get_user():
  name = request.args.get('name') # get방식 파라미터 값 받기
  print('name:',name)
  if name:
    return f"<h1>전달받은 이름 {name}님 반갑습니다</h1>"
  else:
    abort(404)
# 404 에러페이지 처리(404 예외페이지 처리)
@app.errorhandler(404)
def errorHandler(error):
  return render_template("error_page.html"), 404

if __name__=="__main__":
  app.run(debug=True, port=80)