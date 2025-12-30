# pip install pymysql

import pymysql
conn = pymysql.connect(
    host='외부주소',      # 예: '127.0.0.1' 또는 공인IP
    port=3306,
    user='userid',
    password='pw',
    db='devdb',
    charset='utf8'
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM personal order by pno")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()