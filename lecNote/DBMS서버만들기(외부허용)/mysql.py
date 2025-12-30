# pip install pymysql

import pymysql
conn = pymysql.connect(
    host='210.121.189.12',      # 예: '127.0.0.1' 또는 공인IP
    port=3306,
    user='remoteuser',
    password='mbcacademy0212!',
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