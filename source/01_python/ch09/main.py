from customer import load_customers, fn1_insert_customer_info
from customer import fn2_print_customers, fn3_delete_customer
from customer import fn4_search_customer, fn5_save_customer_csv
from customer import fn9_save_customer_txt
def main():
    global customer_list
    customer_list = load_customers() # ch09_customers.txt의 내용을 load
    while True:
        print("1:입력","2:전체출력","3:삭제","4:이름찾기","5:내보내기(CSV)", "9:종료", 
              sep=' | ', end=' ')
        fn = int(input('메뉴선택 : '))
        if fn == 1:
            customer = fn1_insert_customer_info() # 입력받은 내용으로 customer객체를 반환
            customer_list.append(customer)
        elif fn == 2:
            fn2_print_customers(customer_list) # 전체 customer_list 출력
        elif fn == 3:
            fn3_delete_customer(customer_list) # 이름으로 삭제
        elif fn == 4:
            fn4_search_customer(customer_list) # 이름검색
        elif fn == 5:
            fn5_save_customer_csv(customer_list) # csv 백업
        elif fn == 9:
            fn9_save_customer_txt(customer_list) # txt 백업
            break
if __name__ == '__main__':
    main()