### Jinja2 Templates 문법 ###
# 1. 변수 : {{var}} 또는 {{var | filter}} 사용
  # 기본 제공 필터 : lower, upper, length, capitalize, title, trim, replace
  # 형변환 제공 필터 : int, float, string
# 2. 제어문 {% %}
## 2-1 조건문 {% if 조건 %}A태그{%elif 조건 %}
## 2-2 반복문