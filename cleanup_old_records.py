import pymysql
from datetime import datetime, timedelta

connection = pymysql.connect(host='host', user='user', password='password', database='database')
days_old = 30

def cleanup_old_records():
    threshold_date = datetime.now() - timedelta(days=days_old)
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM table WHERE created_at < %s", (threshold_date,))
    connection.commit()

cleanup_old_records()
