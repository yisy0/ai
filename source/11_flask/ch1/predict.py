# predict.py 파일
# 가상환경 만들기 : python -m venv .venv : .venv가상환경 생성
# 가상환경 들어가기 : .venv\Scripts\activate
# pip업그레이드 : python -m pip install --upgrade pip

# pip install statsmodels joblib
# pip install xlwings
# pip install flask

# .gitignore파일에 .venv/와  .idea/추가

# pip freeze > requirements.txt
# requirements.txt 팀원끼리 공유
# requirements.txt있는 라이브러리를 똑같이 설치 : pip install -r requirements.txt

import joblib
loaded_model = joblib.load('model/apt.joblib')
def predict_apt_price(year, square, floor):  
  input_data = [[int(year), int(square), int(floor), 1]]
  result = round(loaded_model.predict(input_data)[0] * 10000)
  return format(result, ',') + '원입니다'
if __name__=="__main__":
  year = input('몇년?')
  square = input('몇 제곱미터?')
  floor = input('몇층?')
  print('예측한 금액은 ', predict_apt_price(year, square, floor))