# pip install cx_oracle (oracle 11g까지)
# pip install oracledb (oracle 12부터)

# 방법1. 공인 IP나 DDNS 주소
# import cx_Oracle
# dsn = cx_Oracle.makedsn("외부주소", 1521, service_name="xe")
# conn = cx_Oracle.connect(user="scott", password="tiger", dsn=dsn)
# 방법2. 
# conn = cx_Oracle.connect("scott", "tiger", "외부주소:1521/xe")
# 방법3
import oracledb
oracledb.init_oracle_client()
# conn = oracledb.connect("scott/tiger@localhost:1521/xe")
conn = oracledb.connect(
    user="scott",
    password="tiger",
    host="외부주소",
    port=1521,
    sid="xe"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM emp")
for row in cursor:
    print(row)

cursor.close()
conn.close()