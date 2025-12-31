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
  return render_template('index.html')