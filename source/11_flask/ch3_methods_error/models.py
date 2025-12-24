from pydantic import BaseModel, Field
class Member(BaseModel):
  name:str = Field(min_length=2, max_length=10, description="이름")