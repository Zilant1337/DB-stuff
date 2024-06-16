import orm_random
from RandomGenerators import *
from database import *
from orm import *
from orm_random import *
import time

copy_database_with_foreign_keys('mydb','clonedb')

db = Database(host='localhost', user='root', password='root', database='clonedb')
db.connect()

a = Employee.create(db, names = "ГЛАВРЫБА", birth_date= "2003-01-23")
print (a.id,a.names,a.birth_date)
a.names = "GAVNO"
a.save()

print (a.id,a.names,a.birth_date)


db.disconnect()