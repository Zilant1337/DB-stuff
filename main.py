import mysql.connector
from RandomGenerators import *

mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    password='root',
    database='mydb'
)
mycursor=mydb.cursor()
mycursor.execute("SELECT COUNT(id) FROM mydb.purchase")
data=mycursor.fetchall()
for row in data:
    print(row)
mycursor.close()
