from lib.RandomGenerators import *
from lib.orm import *

def generate_random_objects(cls, n, db):
    """
    Генерирует n случайных объектов заданного класса и сохраняет их в базе данных.

    Аргументы:
        cls (class): Класс модели, объекты которого нужно создать.
        n (int): Количество объектов для создания.
        db (Database): Объект базы данных для сохранения объектов.

    Возвращает:
        list: Список созданных объектов.
    """
    conn = mysql.connector.connect(host=db.host, user=db.user, password=db.password, database=db.database)
    cursor = conn.cursor()
    created_objects = []
    for _ in range(n):
        if cls == Employee:
            obj_data = RandomEmployee()
        elif cls == Developer:
            obj_data = RandomDeveloper()
        elif cls == Buyer:
            cursor.execute(f"SELECT COUNT(*) FROM {db.database}.platform")
            platformIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {db.database}.genre")
            genreIdLimit = cursor.fetchone()[0]
            obj_data = RandomBuyer(platformIdLimit, genreIdLimit)
        elif cls == Platform:
            obj_data = RandomPlatform()
        elif cls == Genre:
            obj_data = RandomGenre()
        elif cls == Purchase:
            cursor.execute(f"SELECT COUNT(*) FROM {db.database}.game")
            gameIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {db.database}.employee")
            employeeIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {db.database}.buyer")
            buyerIdLimit = cursor.fetchone()[0]
            obj_data = RandomPurchase(gameIdLimit, employeeIdLimit, buyerIdLimit)
        elif cls == Game:
            cursor.execute(f"SELECT COUNT(*) FROM {db.database}.platform")
            platformIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {db.database}.genre")
            genreIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {db.database}.developer")
            developerIdLimit = cursor.fetchone()[0]
            obj_data = RandomGame(platformIdLimit, genreIdLimit, developerIdLimit)
        else:
            raise ValueError(f"Unsupported class: {cls}")
        created_objects.append(cls.create(db,**obj_data))
    return created_objects