import mysql
from matplotlib import pyplot as plt
import time
from lib import database
from functools import partial
import timeit

database.copy_database_with_foreign_keys('mydb','clonedb')

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
        times= timeit.Timer(partial(database.add_random_data,(table_name,1))).repeat(execution_amount)
        table_average_time+= min(times)/execution_amount
    table_average_time/=len(table_names)
    print(table_average_time)
    adding_execution_times.append(table_average_time)
# for execution_amount in command_execution_amounts:
#     table_average_time=0
#     for table_name in table_names:
#         start_time=time.time_ns()
#         database.replace_all_entries(table_name,execution_amount)
#         table_average_time+=time.time_ns()-start_time
#     table_average_time/len(table_names)
#     replacing_execution_times.append(table_average_time)
#
# deletion_average_time=0
# for table_name in table_names:
#     start_time=time.time_ns()
#     database.add_random_data(table_name,execution_amount)
#     deletion_average_time=time.time_ns()-start_time
#     deleting_execution_times.append(deletion_average_time)
#
# print(command_execution_amounts)
# print(adding_execution_times)
# print(replacing_execution_times)
# print(deleting_execution_times)
#
# plt.title("Время выполнения добавления случайных значений в базу данных в зависимости от количества")
# plt.xlabel("Количество")
# plt.ylabel("Время выполнения")
# plt.plot(command_execution_amounts,adding_execution_times,linestyle='--', marker='o', color='b')
# plt.show()
#
# plt.title("Время выполнения замены значений на случайные в базе данных в зависимости от количества")
# plt.xlabel("Количество")
# plt.ylabel("Время выполнения")
# plt.plot(command_execution_amounts,replacing_execution_times, linestyle='--', marker='o', color='b')
# plt.show()
#
# plt.title("Время выполнения очистки таблицы базы данных")
# plt.xlabel("Количество")
# plt.ylabel("Время выполнения")
# plt.plot(table_names,deleting_execution_times)
# plt.show()