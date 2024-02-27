import random
import string
from faker import Faker
from datetime import datetime, timedelta

fake=Faker()
names=["Анна", "Мария", "Елена", "Ольга", "Светлана", "Наталья", "Екатерина", "Татьяна", "Ирина", "Лариса","Алексей", "Дмитрий", "Сергей", "Иван", "Андрей", "Владимир", "Николай", "Артем", "Михаил", "Павел"]

def RandomPurchase(GameIdLimit, EmployeeIdLimit, BuyerIdLimit):

    return ([fake.date_between(start_date='-1y',end_date='now'),random.randint(1,5),random.randint(1,GameIdLimit),random.randint(1,EmployeeIdLimit),random.randint(1,BuyerIdLimit)])

def RandomEmployee():
    global names

    birthDateMin=datetime(year=1970,month=1,day=1)

    return(names[random.randint(0,len(names)-1)],fake.date_between(start_date=birthDateMin,end_date='-18y'))

def RandomBuyer(PlatformIdLimit,GenreIdLimit):
    global names

    birthDateMin = datetime(year=1970, month=1, day=1)

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))

    return (names[random.randint(0,len(names)-1)],password,fake.date_between(start_date=birthDateMin,end_date='-10y'),random.randint(1,PlatformIdLimit),random.randint(1,GenreIdLimit),random.randint(0,999))
