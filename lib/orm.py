import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from lib import models
from lib import orm_random

"""URL для подключения к базе данных"""
DATABASE_URL = 'mysql+mysqlconnector://root:root@localhost/clonedb'

"""Создание объекта engine для подключения к базе данных"""
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
def init_db(engine):
    """
    Инициализирует базу данных, создавая все таблицы, определенные в моделях.

    Аргументы:
        engine (Engine): Экземпляр SQLAlchemy Engine, используемый для подключения к базе данных.
    """
    Base.metadata.create_all(engine)

"""Инициализация базы данных"""
init_db(engine)

def get_all_entries(session, model):
    """
    Возвращает все записи из указанной модели базы данных.

    Аргументы:
        session (Session): Сессия SQLAlchemy.
        model (Base): Модель базы данных.

    Возвращает:
        List[Base]: Список всех записей указанной модели базы данных.

    Исключения:
        sqlalchemy.exc.SQLAlchemyError: В случае ошибки при выполнении запроса.
    """
    try:
        entries = session.query(model).all()
        return entries
    except Exception as e:
        print(f"Ошибка при получении записей: {e}")
        return []

def add_data(session,data):
    """
    Добавляет запись в указанную модель базы данных.

    Аргументы:
        session (Session): Сессия SQLAlchemy.
        model (Base): Модель базы данных.
        data (dict): Данные для добавления в виде словаря.
    """
    session.add(data)
    session.commit()
    print("Запись успешно добавлена")

def add_random_data(session, model, count):
    """
    Добавляет несколько случайных записей в указанную модель базы данных.

    Аргументы:
        session (Session): Сессия SQLAlchemy.
        model (Base): Модель базы данных.
        count (int): Количество записей для добавления.
    """
    for _ in range(count):
        if model == models.Purchase:
            game_id_limit = session.query(models.Game).count()
            employee_id_limit = session.query(models.Employee).count()
            buyer_id_limit = session.query(models.Buyer).count()
            data = orm_random.RandomPurchase(game_id_limit, employee_id_limit, buyer_id_limit)
            add_data(session, data)
        elif model == models.Employee:
            data = orm_random.RandomEmployee()
            add_data(session, data)
        elif model == models.Buyer:
            platform_id_limit = session.query(models.Platform).count()
            genre_id_limit = session.query(models.Genre).count()
            data = orm_random.RandomBuyer(platform_id_limit, genre_id_limit)
            add_data(session, data)
        elif model == models.Game:
            platform_id_limit = session.query(models.Platform).count()
            genre_id_limit = session.query(models.Genre).count()
            developer_id_limit = session.query(models.Developer).count()
            data = orm_random.RandomGame(platform_id_limit, genre_id_limit, developer_id_limit)
            add_data(session, data)
        elif model == models.Platform:
            data = orm_random.RandomPlatform()
            add_data(session, data)
        elif model == models.Developer:
            data = orm_random.RandomDeveloper()
            add_data(session,data)
        elif model == models.Genre:
            data = orm_random.RandomGenre()
            add_data(session,data)

def delete_entry(session, model, entry_id):
    """
    Удаляет конкретную запись из указанной модели базы данных.

    Аргументы:
        session (Session): Сессия SQLAlchemy.
        model (Base): Модель базы данных.
        entry_id (int): ID записи для удаления.
    """
    obj = session.query(model).get(entry_id)
    session.delete(obj)
    session.commit()
    print("Запись успешно удалена")

def delete_all_entries(session, model):
    """
    Удаляет все записи из указанной модели базы данных.

    Аргументы:
        session (Session): Сессия SQLAlchemy.
        model (Base): Модель базы данных.
    """
    session.query(model).delete()
    session.commit()
    print(f"Все записи в {model.__tablename__} успешно удалены")

def replace_all_entries(session, model, count):
    """
    Заменяет все записи в указанной модели новыми случайными данными.

    Аргументы:
        session (Session): Сессия SQLAlchemy.
        model (Base): Модель базы данных.
        count (int): Количество новых записей для добавления.
    """
    delete_all_entries(session, model)
    add_random_data(session, model, count)
    print(f"Replaced all data in {model.__tablename__} with {count} random entries successfully")

# Пример использования:
# session = Session()
# add_random_data(session, Game, 10)
# delete_entry(session, Game, 1)
# delete_all_entries(session, Game)
# replace_all_entries(session, Game, 10)
# session.close()
