# 파일명을 app.py일 경우 실행 : flask run --port 8090 --debug
from flask import Flask, render_template, request
from models import Member
from filters import mask_password

app = Flask(__name__)
app.template_filter("mask_pw")(mask_password) # 필터 추가
@app.errorhandler(404) # 예외 페이지 처리
def errorhandler(error):
  print('★', error)
  return render_template("error_page.html")

@app.route("/", methods=["GET"])
def index():
  return render_template("2_crud/index.html")

@app.route("/join", methods=["GET", "POST"])
def join():
  print(request.method)
  if request.method == "GET":
    return render_template("2_crud/join.html")
  elif request.method == 'POST':
    print(request.form) # POST방식으로 전달된 파라미터 내용
    print(request.form.to_dict())
    return request.form.to_dict()