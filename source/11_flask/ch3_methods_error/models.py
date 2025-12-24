from pydantic import BaseModel, Field
class Member(BaseModel):
  # gt=0:id>0 / gt=0:id>=0 / lt=0; id<0 / le=0;id<=0
  name:str = Field(min_length=2, max_length=10, description="이름")
  id:int   = Field(gt=0, description="숫자id")
  pw:str   = Field(min_length=1)
  addr:str = Field(min_length=1, default="서울", description="주소")
if __name__=="__main__":
  member = Member(name="홍길동", id="1", pw="aa")
  print(member)
