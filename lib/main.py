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

a= generate_random_objects(Game,1,db)
new_game = Game.create(db,**a[0])
print (a)


db.disconnect()