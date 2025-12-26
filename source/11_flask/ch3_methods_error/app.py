# 파일명을 app.py일 경우 실행 : flask run --port 8090 --debug
from flask import Flask, render_template, request
from models import Member
from filters import mask_password

app = Flask(__name__)
app.template_filter("mask_pw")(mask_password) # 필터 추가
@app.errorhandler(404) # 예외 페이지 처리
def errorhandler(error):
  print('★', error)
  return render_template("error_page.html"), 404

@app.route("/", methods=["GET"])
# def index():
#   return render_template("2_crud/index.html")

@app.route("/join", methods=["GET", "POST"])
def join():
  print(request.method)
  if request.method == "GET":
    return render_template("2_crud/join.html")
  elif request.method == 'POST':
    # print(request.form) # POST방식으로 전달된 파라미터 내용
    # name = request.form['name']
    # id   = request.form.get('id')
    # pw   = request.form.get('pw')
    # addr = request.form.get('addr')
    try:
      # member = Member(name=name, id=id, pw=pw, addr=addr)
      member = Member(**request.form.to_dict())
    except Exception as e:
      print(f"유효성 실패 : {e}")
      return render_template("2_crud/join.html",
                            msg="유효한 데이터를 입력하지 않았습니다",
                            form_data=request.form)
    return render_template("2_crud/result.html", member=member)
  
@app.route("/update/<name>/<id>/<pw>/<addr>", methods=["PUT"])
def update(name, id, pw, addr):
  return f"{name}님 정보가 수정되었습니다"

@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
  return f"id가 {id}인 회원정보가 삭제되었습니다"