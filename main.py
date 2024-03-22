import mysql.connector
import subprocess
from matplotlib import pyplot as plt
from RandomGenerators import *

mysqlPath=r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
mysqldumpPath=r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe"
def copy_database_with_foreign_keys(source_database, target_database, host='localhost', user='root', password='root'):
    global mysqldumpPath,mysqlPath
    try:
        # Use mysqldump to create a dump of the source database
        dump_cmd = [
            mysqldumpPath,
            '--single-transaction',
            '-h', host,
            '-u', user,
            '-p' + password,
            source_database,
            '>', f'{source_database}.sql'
        ]

        subprocess.run(dump_cmd, shell=True, check=True)

        # Use mysql command to restore the dump into the target database
        restore_cmd = [
            mysqlPath,
            '-h', host,
            '-u', user,
            '-p' + password,
            target_database,
            '<', f'{source_database}.sql'
        ]

        subprocess.run(restore_cmd, shell=True, check=True)

        print(f"Database '{source_database}' copied to '{target_database}' successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def add_data(table, data,database='clonedb',host='localhost',user='root',password='root'):
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=conn.cursor()
    try:
        columns=", ".join(data.keys())
        values=", ".join(f"'{value}'"for value in data.values())
        query=f'INSERT INTO {table}({columns}) VALUES({values})'

        cursor.execute(query)
        conn.commit()
        print("Entry added successfully")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cursor.close()
        conn.close()

def add_random_data(table,count,database='clonedb',host='localhost',user='root',password='root'):
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    for i in range (count):
        if(table=="purchase"):
            cursor.execute(f"SELECT COUNT(*) FROM {database}.game")
            gameIdLimit=cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {database}.employee")
            employeeIdLimit=cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {database}.buyer")
            buyerIdLimit= cursor.fetchone()[0]
            data=RandomPurchase(gameIdLimit,employeeIdLimit,buyerIdLimit)
            add_data(table,data)
        if(table=="employee"):
            data=RandomEmployee()
            add_data(table,data)
        if(table=="buyer"):
            cursor.execute(f"SELECT COUNT(*) FROM {database}.platform")
            platformIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {database}.genre")
            genreIdLimit = cursor.fetchone()[0]
            data=RandomBuyer(platformIdLimit,genreIdLimit)
            add_data(table,data)
        if(table=="game"):
            cursor.execute(f"SELECT COUNT(*) FROM {database}.platform")
            platformIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {database}.genre")
            genreIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {database}.developer")
            developerIdLimit = cursor.fetchone()[0]
            data=RandomGame(platformIdLimit,genreIdLimit,developerIdLimit)
            add_data(table,data)
        if(table=="platform"):
            data=RandomPlatform()
            add_data(table,data)

def delete_entry(table,index,database='clonedb',host='localhost',user='root',password='root'):
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE id= {index}")
    conn.commit()
    cursor.close()
    conn.close()

def delete_all_entries(table,database='clonedb',host='localhost',user='root',password='root'):
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    cursor.execute(f"TRUNCATE TABLE {table}")
    conn.commit()
    cursor.close()
    conn.close()
def replace_all_entries(table,count,database='clonedb',host='localhost',user='root',password='root'):
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    cursor.execute(f"TRUNCATE TABLE {table}")
    conn.commit()
    add_random_data(table,count,database,host,user,password)
    cursor.close()
    conn.close()

copy_database_with_foreign_keys('mydb','clonedb')

mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    password='root',
    database='clonedb'
)
mycursor=mydb.cursor()
# mycursor.execute("SELECT * FROM clonedb.purchase")
# purchase=mycursor.fetchall()
# mycursor.execute("SELECT * FROM clonedb.platform")
# platform=mycursor.fetchall()
# mycursor.execute("SELECT * FROM clonedb.genre")
# genre=mycursor.fetchall()
# mycursor.execute('SELECT * FROM clonedb.game')
# game=mycursor.fetchall()
# mycursor.execute('SELECT * FROM clonedb.employee')
# employee=mycursor.fetchall()
# mycursor.execute('SELECT * FROM clonedb.developer')
# developer=mycursor.fetchall()
# mycursor.execute('SELECT * FROM clonedb.buyer')
# buyer=mycursor.fetchall()
# print('purchase:\n')
# print(purchase)
# print('platform:\n')
# print(platform)
# print('genre:\n')
# print(genre)
# print('game:\n')
# print(game)
# print('employee:\n')
# print(employee)
# print('developer:\n')
# print(developer)
# print('buyer:\n')
# print(buyer)
mycursor.close()
add_random_data("purchase",1)

# mydb=mysql.connector.connect(
#     host="localhost",
#     user='root',
#     password='root',
#     database='clonedb'
# )
# mycursor=mydb.cursor()
# mycursor.execute('SELECT * FROM clonedb.employee')
# employee=mycursor.fetchall()
# print('employee:\n')
# print(employee)
#
# mycursor.close()
