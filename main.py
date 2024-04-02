import mysql.connector
import subprocess
from matplotlib import pyplot as plt
from RandomGenerators import *
import time

mysqlPath=r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
mysqldumpPath=r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe"
def copy_database_with_foreign_keys(source_database, target_database, host='localhost', user='root', password='root'):
    global mysqldumpPath,mysqlPath
    try:
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
    try:
        cursor.execute(f"DELETE FROM {table} WHERE id= {index}")
        conn.commit()
        print(f"Entry deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cursor.close()
        conn.close()

def delete_all_entries(table,database='clonedb',host='localhost',user='root',password='root'):
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    try:
        cursor.execute(f"TRUNCATE TABLE {table}")
        conn.commit()
        print(f"Deleted all entries in {database}.{table} successfully")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cursor.close()
        conn.close()
def replace_all_entries(table,count,database='clonedb',host='localhost',user='root',password='root'):
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    try:
        cursor.execute(f"TRUNCATE TABLE {table}")
    except mysql.connector.Error as err:
        print(f"Error:{err}\n Deleting purchase and trying again...")
        cursor.execute(f"TRUNCATE TABLE purchase")
    conn.commit()
    try:
        add_random_data(table,count,database,host,user,password)
        print(f"Replaced all data in {database}.{table} with {count} random entries successfully")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cursor.close()
        conn.close()


copy_database_with_foreign_keys('mydb','clonedb')

command_execution_amounts=[]
for i in range(3):
    command_execution_amounts.append(10**i)

adding_execution_times=[]
replacing_execution_times=[]
deleting_execution_times=[]

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="clonedb")
cursor=conn.cursor()

table_names=['employee','buyer','game','platform','purchase']

for execution_amount in command_execution_amounts:
    table_average_time=0
    for table_name in table_names:
        start_time=time.time_ns()
        add_random_data(table_name,execution_amount)
        table_average_time+=time.time_ns()-start_time
        start_time
    table_average_time/len(table_names)
    adding_execution_times.append(table_average_time)
for execution_amount in command_execution_amounts:
    table_average_time=0
    for table_name in table_names:
        start_time=time.time_ns()
        replace_all_entries(table_name,execution_amount)
        table_average_time+=time.time_ns()-start_time
    table_average_time/len(table_names)
    replacing_execution_times.append(table_average_time)

deletion_average_time=0
for table_name in table_names:
    start_time=time.time_ns()
    add_random_data(table_name,execution_amount)
    deletion_average_time=time.time_ns()-start_time
    deleting_execution_times.append(deletion_average_time)

print(command_execution_amounts)
print(adding_execution_times)
print(replacing_execution_times)
print(deleting_execution_times)

plt.title("Время выполнения добавления случайных значений в базу данных в зависимости от количества")
plt.xlabel("Количество")
plt.ylabel("Время выполнения")
plt.plot(command_execution_amounts,adding_execution_times,linestyle='--', marker='o', color='b')
plt.show()

plt.title("Время выполнения замены значений на случайные в базе данных в зависимости от количества")
plt.xlabel("Количество")
plt.ylabel("Время выполнения")
plt.plot(command_execution_amounts,replacing_execution_times, linestyle='--', marker='o', color='b')
plt.show()

plt.title("Время выполнения очистки таблицы базы данных")
plt.xlabel("Количество")
plt.ylabel("Время выполнения")
plt.plot(table_names,deleting_execution_times)
plt.show()

