from matplotlib import pyplot as plt

import orm_random
from RandomGenerators import *
from database import *
from orm import *
from orm_random import *
import time

session = Session()
employee = orm_random.RandomBuyer(10,21)
session.add(employee)
session.commit()
session.close()