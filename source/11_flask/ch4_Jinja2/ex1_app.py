### Jinja2 Templates 문법 ###
# 1. 변수 : {{var}} 또는 {{var | filter}} 사용
  # 기본 제공 필터 : lower, upper, length, capitalize, title, trim, replace
  # 형변환 제공 필터 : int, float, string
# 2. 제어문 {% %}
## 2-1 조건문 {% if 조건1 %}A태그{% elif 조건2 %}B태그{% else %}C태그{% endif %}
## 2-2 반복문
##    {% for var in vars %}
##      <태그>{{loop.index}}. {{var}}</태그>
##        loop.index : 1부터 순번 / loop.first:첫번째 loop인지 여부 / loop.last:마지막 loop인지 여부
##    {% endfor %}
# 3. 해더나 풋터 {% include "header.html" %} {% extends "base.html" %}
# 4. 서브 블럭 {% block %} {% endblock %}
# 5. 주석 {# 주석 #}

from flask import Flask, render_template, request
app = Flask(__name__, static_folder="static", template_folder="templates")
lst = []
# 예외처리 페이지
@app.errorhandler(404)
def not_found(error):
  return render_template("page_not_found.html", error=error), 404 # 콘솔에 404 출력
if __name__ == "__main__":
  app.run(debug=True, port=80)