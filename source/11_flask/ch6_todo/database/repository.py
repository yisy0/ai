from database.connection import conn
from models import Todo
from typing import List # 타입 체크용
# get_todos의 매개변수는 문자로 order를 전달받아 return dict list를 반환
def get_todos(order:str="asc") -> List[dict]: