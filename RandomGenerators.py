import random
import string
from faker import Faker
from datetime import datetime, timedelta

fake=Faker()
names=["Анна", "Мария", "Елена", "Ольга", "Светлана", "Наталья", "Екатерина", "Татьяна", "Ирина", "Лариса","Алексей", "Дмитрий", "Сергей", "Иван", "Андрей", "Владимир", "Николай", "Артем", "Михаил", "Павел"]
gameNames1=["Duty","Call","Open","Guilty","Escape","Jungle","Fun"]
gameNames2=["World","Calls","Gear","Adventure","Escape","Exodus"]
prices=[5,10,20,30,40,60,70,80]
ageRatings=[0,3,7,12,16,18]
languages=["English","Russian", "Japanese", "French","German", "Spanish", "Finnish", "Swedish"]
platform1=["Playstation","Xbox","Nintendo"]
platform2=["2","3","4","5","6","7","8","9","10","One","Switch","Wii","Gamecube","WiiU","360"]
def RandomPurchase(GameIdLimit, EmployeeIdLimit, BuyerIdLimit):

    return ({"dates":fake.date_between(start_date='-1y',end_date='now'),
             "amount":random.randint(1,5),
             "Game_id":random.randint(1,GameIdLimit),
             "Employee_id":random.randint(1,EmployeeIdLimit),
             "Buyer_id":random.randint(1,BuyerIdLimit)})

def RandomEmployee():
    global names

    birthDateMin=datetime(year=1970,month=1,day=1)

    return({"names":names[random.randint(0,len(names)-1)],
            "birth_date":fake.date_between(start_date=birthDateMin,end_date='-18y')})

def RandomBuyer(PlatformIdLimit,GenreIdLimit):
    global names

    birthDateMin = datetime(year=1970, month=1, day=1)

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))

    return ({"names":names[random.randint(0,len(names)-1)],
             "password":password,
             "birth_date":fake.date_between(start_date=birthDateMin,end_date='-10y'),
             "Platform_id":random.randint(1,PlatformIdLimit),
             "Genre_id":random.randint(1,GenreIdLimit),
             "boughtgames":random.randint(0,999)})
def RandomGame(PlatformIdLimit,GenreIdLimit,DeveloperIdLimit):
    global gameNames2, gameNames1
    return {"names":gameNames1[random.randint(0,len(gameNames1)-1)]+" "+gameNames2[random.randint(0,len(gameNames2)-1)],
            "price":prices[random.randint(0,len(prices)-1)],
            "age_rating":ageRatings[random.randint(0,len(ageRatings)-1)],
            "user_rating":random.randint(0,5),
            "release_date": fake.date_between(start_date='-30y', end_date='now'),
            "player_count":random.randint(1,8),
            "language":languages[random.randint(0,len(languages)-1)],
            "stock":random.randint(0,100000),
            "Platform_id":random.randint(1,PlatformIdLimit),
            "Genre_id":random.randint(1,GenreIdLimit),
            "Developer_id":random.randint(1,DeveloperIdLimit)}
def RandomPlatform():
    global platform1, platform2
    return ({"names":platform1[random.randint(0,len(platform1)-1)]+" "+ platform2[random.randint(0,len(platform2)-1)]})

