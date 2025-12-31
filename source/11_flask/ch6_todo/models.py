# pip install pydantic
from pydantic import BaseModel

class Todo(BaseModel):
  id: int | None = None
  content: str
  is_done: bool | None = False

if __name__ == "__main__":
  todo = Todo(content="오늘 할 일")
  print(todo)
  print(todo.model_dump()) # 객체를 딕셔너리형태로 변환