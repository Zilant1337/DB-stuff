import orm_random
from RandomGenerators import *
from database import *
from orm import *
from orm_random import *
import time

copy_database_with_foreign_keys('mydb','clonedb')

db = Database(host='localhost', user='root', password='root', database='clonedb')
db.connect()

Purchase.create(db)

a= Purchase.create(db,dates = "2024-09-21",amount = "10", Game_id= "9", Employee_id = "1", Buyer_id = "1")
a.save()


db.disconnect()