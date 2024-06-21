import pymysql
import csv

connection = pymysql.connect(host='host', user='user', password='password', database='database')

def generate_report():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM table")
        rows = cursor.fetchall()
        with open('report.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([i[0] for i in cursor.description])  # write headers
            csv_writer.writerows(rows)

generate_report()
