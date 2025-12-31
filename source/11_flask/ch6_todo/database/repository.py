from database.connection import conn
from models import Todo
from typing import List # 타입 체크용
# get_todos의 매개변수는 문자로 order를 전달받아 return dict list를 반환
def get_todos(order:str="asc") -> List[dict]:
  cursor = conn.cursor()
  if order == "asc":
    sql = "SELECT * FROM TODO ORDER BY ID"
  else:
    sql = "SELECT * FROM TODO ORDER BY ID DESC"
  cursor.execute(sql)
  result = cursor.fetchall()
  # ["id", "content", "is_done"]
  keys = [desc[0].lower() for desc in cursor.description] 
  todos = [dict(zip(keys, row)) for row in result]
  cursor.close()
  return todos