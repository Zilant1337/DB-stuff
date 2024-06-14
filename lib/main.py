from matplotlib import pyplot as plt

import orm_random
from RandomGenerators import *
from database import *
from orm import *
from orm_random import *
import time

copy_database_with_foreign_keys('mydb','clonedb')

db = Database(host='localhost', user='root', password='root', database='clonedb')
db.connect()

User.create_table(db)

# Создаем нового пользователя и сохраняем его в базе данных
new_employee = Employee.create(db, names='Bob', birth_date= '1990-02-23')

db.disconnect()