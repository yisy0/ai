import cx_Oracle
conn = cx_Oracle.connect("scott", "tiger", "210.121.189.12:1521/xe")
def get_emp_list():
    cursor = conn.cursor()
    sql = "SELECT * FROM EMP"
    cursor.execute(sql)
    emps = cursor.fetchall()
    keys = [desc[0].lower() for desc in cursor.description]
    emp_list = [dict(zip(keys, emp)) for emp in emps]
    return emp_list # 딕셔너리 리스트
def get_emp(empno):
    cursor = conn.cursor()
    sql = "SELECT * FROM EMP WHERE EMPNO = :empno"
    cursor.execute(sql, {'empno': empno})
    emp = cursor.fetchone()
    keys = [desc[0].lower() for desc in cursor.description]
    emp = dict(zip(keys, emp))
    return emp # 딕셔너리
if __name__ == '__main__':
    # emp_list = get_emp_list()
    # print(emp_list)
    emp = get_emp(7902)
    print(emp)

# 실행하는 방법 python -m database.repository