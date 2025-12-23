# static route http://127.0.0.1/login?id=aaa&pw=111 => ch3
# dynamic route http://127.0.0.1/login/aaa/111
from flask import Flask, url_for
app = Flask(__name__)
# 라우팅 : url을 특정 함수에 연결하는 작업
@app.route("/hello") # 정적 라우팅
def hello():
  return "<h1>Hello</h1>"
@app.route("/profile/<username>") # 동적 라우팅
def get_profile(username):
  return "<h1>profile : {}</h1>".format(username)

if __name__== "__main__":
  # 플라스크가 http 요청 관련 정보를 저장하는 요청 컨텍스트 활성화
  with app.test_request_context():
    print('hello 핸들러 함수의 요청경로 :', url_for('hello'))
    print('get_profile 핸들러 함수의 요청경로 :',
          url_for('get_profile', username='hong')
          )
  app.run(debug=True, port=80)