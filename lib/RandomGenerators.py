import random
import string
from faker import Faker
from datetime import datetime

"""Создание объекта Faker для генерации случайных данных"""
fake = Faker()

"""Списки для генерации случайных данных"""
names = ["Анна", "Мария", "Елена", "Ольга", "Светлана", "Наталья", "Екатерина", "Татьяна", "Ирина", "Лариса",
         "Алексей", "Дмитрий", "Сергей", "Иван", "Андрей", "Владимир", "Николай", "Артем", "Михаил", "Павел"]

gameNames1 = ["Duty", "Call", "Open", "Guilty", "Escape", "Jungle", "Fun"]
gameNames2 = ["World", "Calls", "Gear", "Adventure", "Escape", "Exodus"]
prices = [5, 10, 20, 30, 40, 60, 70, 80]
ageRatings = [0, 3, 7, 12, 16, 18]
languages = ["English", "Russian", "Japanese", "French", "German", "Spanish", "Finnish", "Swedish"]
platform1 = ["Playstation", "Xbox", "Nintendo"]
platform2 = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "One", "Switch", "Wii", "Gamecube", "WiiU", "360"]
dev1 = ["Quantum","Pixel","Infinite","Dynamic","Epic","Rogue","Stellar","Arcane","Mythic","Mystic","Titan","Lunar","Thunder","Cyber","Crystal","Nova","Fusion","Dream","Phoenix","Celestial"]
dev2 = ["Forge","Studios","Games","Works","Labs","Creations","Haven","Realm","Ventures","Interactive","Craft","Engine","Arcade","Vision","Dimension","Nexus","Galaxy","Realm","Dynamics","Horizon"]
gameGenres = [
    "Action",
    "Adventure",
    "Role-Playing (RPG)",
    "Simulation",
    "Strategy",
    "Shooter",
    "Puzzle",
    "Platformer",
    "Fighting",
    "Sports",
    "Racing",
    "Stealth",
    "Survival",
    "Horror",
    "Music/Rhythm",
    "Sandbox",
    "Party",
    "Visual Novel",
    "Card Game",
    "Tower Defense"
]

def RandomPurchase(GameIdLimit, EmployeeIdLimit, BuyerIdLimit):
    """
    Генерирует случайную запись о покупке.

    Аргументы:
        GameIdLimit (int): Максимальный ID игры.
        EmployeeIdLimit (int): Максимальный ID сотрудника.
        BuyerIdLimit (int): Максимальный ID покупателя.

    Возвращает:
        dict: Словарь с данными о покупке.
    """
    return {
        "dates": str(fake.date_between(start_date='-1y', end_date='now')),
        "amount": random.randint(1, 5),
        "Game_id": random.randint(1, GameIdLimit),
        "Employee_id": random.randint(1, EmployeeIdLimit),
        "Buyer_id": random.randint(1, BuyerIdLimit)
    }

def RandomEmployee():
    """
    Генерирует случайную запись о сотруднике.

    Возвращает:
        dict: Словарь с данными о сотруднике.
    """
    global names

    birthDateMin = datetime(year=1970, month=1, day=1)

    return {
        "names": names[random.randint(0, len(names) - 1)],
        "birth_date": str(fake.date_between(start_date=birthDateMin, end_date='-18y'))
    }

def RandomBuyer(PlatformIdLimit, GenreIdLimit):
    """
    Генерирует случайную запись о покупателе.

    Аргументы:
        PlatformIdLimit (int): Максимальный ID платформы.
        GenreIdLimit (int): Максимальный ID жанра.

    Возвращает:
        dict: Словарь с данными о покупателе.
    """
    global names

    birthDateMin = datetime(year=1970, month=1, day=1)

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))

    return {
        "names": names[random.randint(0, len(names) - 1)],
        "password": password,
        "birth_date": str(fake.date_between(start_date=birthDateMin, end_date='-10y')),
        "Platform_id": random.randint(1, PlatformIdLimit),
        "Genre_id": random.randint(1, GenreIdLimit),
        "boughtgames": random.randint(0, 999)
    }

def RandomGame(PlatformIdLimit, GenreIdLimit, DeveloperIdLimit):
    """
    Генерирует случайную запись о игре.

    Аргументы:
        PlatformIdLimit (int): Максимальный ID платформы.
        GenreIdLimit (int): Максимальный ID жанра.
        DeveloperIdLimit (int): Максимальный ID разработчика.

    Возвращает:
        dict: Словарь с данными о игре.
    """
    global gameNames2, gameNames1
    return {
        "names": gameNames1[random.randint(0, len(gameNames1) - 1)] + " " + gameNames2[random.randint(0, len(gameNames2) - 1)],
        "price": prices[random.randint(0, len(prices) - 1)],
        "age_rating": ageRatings[random.randint(0, len(ageRatings) - 1)],
        "user_rating": random.randint(0, 5),
        "release_date": str(fake.date_between(start_date='-30y', end_date='now')),
        "player_count": random.randint(1, 8),
        "language": languages[random.randint(0, len(languages) - 1)],
        "stock": random.randint(0, 100000),
        "Platform_id": random.randint(1, PlatformIdLimit),
        "Genre_id": random.randint(1, GenreIdLimit),
        "Developer_id": random.randint(1, DeveloperIdLimit)
    }

def RandomPlatform():
    """
    Генерирует случайную запись о игровой платформе.

    Возвращает:
        dict: Словарь с данными о платформе.
    """
    global platform1, platform2
    return {
        "names": platform1[random.randint(0, len(platform1) - 1)] + " " + platform2[random.randint(0, len(platform2) - 1)]
    }
def RandomDeveloper():
    """
        Генерирует случайную запись о разработчике.

        Возвращает:
            dict: Словарь с данными о разработчике.
    """
    global dev1,dev2
    return {
        "names": dev1[random.randint(0, len(dev1) - 1)] + " " + dev2[random.randint(0, len(dev2) - 1)],
        "user_rating" : random.randint(0,5)
    }
def RandomGenre():
    """
        Генерирует случайную запись о жанре.

        Возвращает:
            dict: Словарь с данными о жанре.
    """
    global gameGenres
    return {
        "names": gameGenres[random.randint(0,len(gameGenres)-1)]
    }