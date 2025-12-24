# Member 정보를 출력할 경우 비밀번호는 '*'로 대체해서 출력
def mask_password(password):
  return '*'*len(password)
if __name__=="__main__":
  password = input('비밀번호는 ?')
  print('비밀번호 :', password)
  print('비밀번호 :', mask_password(password))