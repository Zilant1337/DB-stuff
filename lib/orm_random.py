import random
from datetime import datetime
import string
from faker import Faker
from lib import models

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

def RandomEmployee():
    """
    Генерирует случайную запись о сотруднике.

    Возвращает:
        Employee: Объект класса Employee с данными о сотруднике.
    """
    birthDateMin = datetime(year=1970, month=1, day=1)

    return models.Employee(
        names=names[random.randint(0, len(names) - 1)],
        birth_date=fake.date_between(start_date=birthDateMin, end_date='-18y')
    )

def RandomPurchase(GameIdLimit, EmployeeIdLimit, BuyerIdLimit):
    """
    Генерирует случайную запись о покупке.

    Аргументы:
        GameIdLimit (int): Максимальный ID игры.
        EmployeeIdLimit (int): Максимальный ID сотрудника.
        BuyerIdLimit (int): Максимальный ID покупателя.

    Возвращает:
        Purchase: Объект класса Purchase с данными о покупке.
    """
    return models.Purchase(
        date=fake.date_between(start_date='-5y', end_date='now'),
        amount=random.randint(1, 10),
        game_id=random.randint(1, GameIdLimit),
        employee_id=random.randint(1, EmployeeIdLimit),
        buyer_id=random.randint(1, BuyerIdLimit)
    )

def RandomBuyer(PlatformIdLimit, GenreIdLimit):
    """
    Генерирует случайную запись о покупателе.

    Аргументы:
        PlatformIdLimit (int): Максимальный ID платформы.
        GenreIdLimit (int): Максимальный ID жанра.

    Возвращает:
        Buyer: Объект класса Buyer с данными о покупателе.
    """
    birthDateMin = datetime(year=1970, month=1, day=1)

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))

    return models.Buyer(
        names=names[random.randint(0, len(names) - 1)],
        password=password,
        birth_date=fake.date_between(start_date=birthDateMin, end_date='-10y'),
        platform_id=random.randint(1, PlatformIdLimit),
        genre_id=random.randint(1, GenreIdLimit),
        boughtgames=random.randint(0, 999)
    )

def RandomGame(PlatformIdLimit, GenreIdLimit, DeveloperIdLimit):
    """
    Генерирует случайную запись о игре.

    Аргументы:
        PlatformIdLimit (int): Максимальный ID платформы.
        GenreIdLimit (int): Максимальный ID жанра.
        DeveloperIdLimit (int): Максимальный ID разработчика.

    Возвращает:
        Game: Объект класса Game с данными о игре.
    """
    return models.Game(
        names=gameNames1[random.randint(0, len(gameNames1) - 1)] + " " + gameNames2[random.randint(0, len(gameNames2) - 1)],
        price=prices[random.randint(0, len(prices) - 1)],
        age_rating=ageRatings[random.randint(0, len(ageRatings) - 1)],
        user_rating=random.uniform(0, 5),
        release_date=fake.date_between(start_date='-30y', end_date='now'),
        player_count=random.randint(1, 8),
        language=languages[random.randint(0, len(languages) - 1)],
        stock=random.randint(0, 100000),
        platform_id=random.randint(1, PlatformIdLimit),
        genre_id=random.randint(1, GenreIdLimit),
        developer_id=random.randint(1, DeveloperIdLimit)
    )

def RandomPlatform():
    """
    Генерирует случайную запись о игровой платформе.

    Возвращает:
        Platform: Объект класса Platform с данными о платформе.
    """
    return models.Platform(
        names=platform1[random.randint(0, len(platform1) - 1)] + " " + platform2[random.randint(0, len(platform2) - 1)]
    )
