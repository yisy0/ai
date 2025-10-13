class Customer:
    '고객 데이터'
    def __init__(self, name, phone, email, age, grade, etc):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.grade = grade
        self.etc = etc
    def as_dic(self):
        return self.__dict__
    def to_txt_style(self):
        return "{}, {}, {}, {}, {}, {}".format(self.name, self.phone, self.email,
                                              self.age, self.grade, self.etc)
    def __str__(self):
        return "{:>5}\t{:^3}\t{:^13}\t{:^10}\t{}\t{}".format('*'*self.grade,
                                                    self.name,
                                                    self.phone,
                                                    self.email,
                                                    self.age,
                                                    self.etc)
    
def to_customer(text):
    'txt 파일 내용 한줄(홍길동, 010-8999-9999, e@e.com, 20, 3, 까칠해)을 Customer 객체로 반환'
    data = text.strip().split(', ')
    name = data[0]
    phone = data[1]
    email = data[2]
    age = int(data[3])
    grade = int(data[4])
    etc = data[5]
    return Customer(name, phone, email, age, grade, etc)

def load_customers():
    customer_list = []
    # 파일 내용을 customer_list에 append한다. 예외발생시 파일 작성
    try:
        with open('data/ch09_customers.txt', 'r', encoding='utf-8') as f:
            # 방법1. 한줄씩 읽어서 customer_list에 append하기
#             line = f.readline()
#             while line != '':
#                 customer = to_customer(line)
#                 customer_list.append(customer)
#                 line = f.readline()
            # 방법2. 여러줄을 한꺼번에 읽어서 for문으로 append하기
            lines = f.readlines()
        for line in lines:
            customer = to_customer(line)
            customer_list.append(customer)
    except FileNotFoundError as e:
        with open('data/ch09_customers.txt', 'w', encoding='utf-8') as f:
            f.write('')
    return customer_list

def fn1_insert_customer_info():
    'name(정규표현식 검증), phone, email, age, grade, etc입력받아 Customer형 객체 return'
    import re
    name = input('이름 :')
    name_pattern = r'[가-힣]{2,}'
    while not re.search(name_pattern, name):
        print('이름을 제대로 입력하세요(한글 2글자 이상)')
        name = input('이름 :')
    phone = input('전화 :')
#     phone_pattern = r'\d{2,3}[ \-\.)]?\d{3,4}[ \-\.]?\d{4}'
#     while not re.search(phone_pattern, phone):
#         print('이름을 제대로 입력하세요(한글 2글자 이상)')
#         phone = input('전화 :')
    email = input('메일 :')
    while True:
        try:
            age = int(input('나이 :'))
            if (age<0) or (age>130) :
                raise Exception('나이 범위 이상')
            break 
        except:
            print('올바른 나이를 입력하세요')
    try:
        grade = int(input('등급(1~5) : '))
        # grade = 1 if grade < 1 else 5 if grade>5 else grade
        if grade < 1:
            grade = 1
        if grade > 5:
            grade = 5
    except:
        print('유효하지 않은 등급 입력시 1등급으로 초기화')
        grade = 1
    etc = input('기타 정보 :')
    return Customer(name, phone, email, age, grade, etc)

def fn2_print_customers(customer_list):
    'customer_list 출력'
    print('='*70)
    print('{:^70}'.format('고객 정보'))
    print('='*70)
    print("{:>5}\t{:^3}\t{:^13}\t{:^10}\t{}\t{}".format('grade','이름','전화','메일','나이','기타') )
    print('-'*70)
    for customer in customer_list:
        print(customer)

def fn3_delete_customer(customer_list):
    '삭제하고자 하는 고객이름을 받아 customer_list에서 삭제(지울지 묻고 지우기)'
    name = input('삭제할 고객의 이름은?')
    delete_idx = [] # 삭제할 인덱스 저장 용도
    cnt = 0 # 지울 고객 수 count
    for idx, customer in enumerate(customer_list):
        if customer.name == name:
            delete_idx.append(idx) # 삭제할 인덱스 추가함
    if delete_idx:
        for idx in delete_idx[::-1]: # [4, 1, 0]
            print(customer_list[idx], '를 지우겠습니까(Y/N)?')
            answer = input()
            if answer.replace('네','y').upper() == 'Y':
                cnt += 1
                del customer_list[idx]
        print(f'{name}님 {cnt}명을 삭제하였습니다')
    else:
        print(name, '님이 데이터에 존재하지 않습니다')

def fn4_search_customer(customer_list):
    '찾고자 하는 이름을 input받아, customer_list에서 검색하여 fn2_print_customers()이용하여 출력'
    name = input('검색할 이름은?')
    search_list = [] # 검색한 결과 append
    for customer in customer_list:
        if customer.name == name:
            search_list.append(customer)
    if search_list:
        fn2_print_customers(search_list)
    else:
        print(f"{name}님 데이터는 존재하지 않습니다")

def fn5_save_customer_csv(customer_list):
    '매개변수로 받은 customer_list를 딕셔너리리스트로 변환하여 csv출력'
    import csv
    if customer_list:
        customer_dict_list = []
        for customer in customer_list:
            customer_dict_list.append(customer.__dict__)
        fieldnames = list(customer_dict_list[0].keys())
        filename = input('저장할 csv파일명은(확장자제외)?')
        with open('data/{}.csv'.format(filename), 'w', encoding='UTF-8', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            dict_writer.writeheader() # 해더 쓰기
            dict_writer.writerows(customer_dict_list) # 데이터 쓰기
            print(f'data/{filename}.csv 내보내기 완료')
    else:
        print('입력된 회원 데이터가 없어서 csv 내보내기를 취소합니다')

def fn9_save_customer_txt(customer_list):
    'customer_list의 내용을 data/ch09_customers.txt에 저장'
    customer_text_list = []
    for customer in customer_list:
        customer_text_list.append(customer.to_txt_style()+"\n")
    with open('data/ch09_customers.txt', 'w', encoding='UTF-8') as f:
        f.writelines(customer_text_list)