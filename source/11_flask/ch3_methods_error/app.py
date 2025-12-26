# 파일명을 app.py일 경우 실행 : flask run --port 8090 --debug
from flask import Flask, render_template, request
from models import Member
from filters import mask_password

app = Flask(__name__)
app.template_filter("mask_pw")(mask_password) # 필터 추가
@app.errorhandler(404)