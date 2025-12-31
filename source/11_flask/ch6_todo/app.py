# 가상환경 만들기 : python -m venv .venv
# 가상환경 들어가기 : .venv\Scripts\activate
# python -m pip install --upgrade pip
# pip install flask pydantic cx_Oracle python-dotenv
# pip freeze > requirements.txt
# pip install -r requirements.txt

from flask import Flask, request, render_template
from database.repository import get_todos, get_next_id, get_todo
from database.repository import create_todo, update_todo, delete_todo
from flask import redirect, url_for, abort
from flask import session #  로그인/로그아웃
from models import Todo

app = Flask(__name__)
#app.secret_key = "abc123!" # 세션을 사용할 경우 필수
app.config['SECRET_KEY'] = 'abc123!'

@app.route('/')
def index():
  "로그인 성공 로직(세션에 로그인 정보 저장)후 /todos로 이동"
  session["user_id"]="hong"
  session["user_name"] = "홍길동"
  # return redirect("/todos") # /todos 요청경로로 이동
  return redirect(url_for("todos")) # todos 함수로 이동
@app.route('/logout')
def logout():
  "로그아웃 로직(세션 정보 제거)후 /todos로 이동"
  session.pop("user_id", None)
  session.pop("user_name", None)
  return redirect(url_for("todos")) # todos 함수로 이동
@app.route('/todos')
def todos():
  "todo 목록 보여주기"
  order = request.args.get("order", "asc") # GET방식 요청
  todos = get_todos(order)
  next_id = get_next_id()
  return render_template("todo/todos.html", 
                        todos=todos, 
                        next_id=next_id)
