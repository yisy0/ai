# 웹서버 생성 및 실행, url(/apt/2025/106/9) 요청시 집값
from flask import Flask
from predict import loaded_model, predict_apt_price

application = Flask(__name__) # 웹 서버(웹 어플리케이션 객체)
@application.route('/')
def handler_function():
  return "<h1>Hello</h1>"
@application.route('/apt/<year>/<square>/<floor>')
def aptPredictHandler(year, square, floor):
  answer = predict_apt_price(year, square, floor)
  return "<h1>예측 금액은 {}<h1>".format(answer)
if __name__=="__main__":
  application.run(debug=True) # 서버실행(소스 변경시 서버 자동 재시작)