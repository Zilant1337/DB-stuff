from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    names = Column(String)

class Developer(Base):
    __tablename__ = 'developer'
    id = Column(Integer, primary_key=True)
    names = Column(String)
    user_rating = Column(Float)

class Game(Base):
    """
    Класс Game представляет таблицу игр в базе данных.

    Атрибуты:
        id (int): Первичный ключ.
        name (str): Название игры.
        price (float): Цена игры.
        age_rating (int): Возрастной рейтинг игры.
        user_rating (float): Оценка пользователей.
        release_date (date): Дата выпуска игры.
        player_count (int): Количество игроков.
        language (str): Язык игры.
        stock (int): Количество доступных копий.
        platform_id (int): Внешний ключ, связывающий с таблицей платформ.
        genre_id (int): Внешний ключ, связывающий с таблицей жанров.
        developer_id (int): Внешний ключ, связывающий с таблицей разработчиков.
    """
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    names = Column(String)
    price = Column(Float)
    age_rating = Column(Integer)
    user_rating = Column(Float)
    release_date = Column(Date)
    player_count = Column(Integer)
    language = Column(String)
    stock = Column(Integer)
    platform_id = Column(Integer, ForeignKey('platform.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    developer_id = Column(Integer, ForeignKey('developer.id'))

class Employee(Base):
    """
    Класс Employee представляет таблицу сотрудников в базе данных.

    Атрибуты:
        id (int): Первичный ключ.
        name (str): Имя сотрудника.
        birth_date (date): Дата рождения сотрудника.
    """
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    names = Column(String)
    birth_date = Column(Date)

class Buyer(Base):
    """
    Класс Buyer представляет таблицу покупателей в базе данных.

    Атрибуты:
        id (int): Первичный ключ.
        name (str): Имя покупателя.
        password (str): Пароль покупателя.
        birth_date (date): Дата рождения покупателя.
        platform_id (int): Внешний ключ, связывающий с таблицей платформ.
        genre_id (int): Внешний ключ, связывающий с таблицей жанров.
        bought_games (int): Количество купленных игр.
    """
    __tablename__ = 'buyer'
    id = Column(Integer, primary_key=True)
    names = Column(String)
    password = Column(String)
    birth_date = Column(Date)
    platform_id = Column(Integer, ForeignKey('platform.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    boughtgames = Column(Integer)

class Platform(Base):
    """
    Класс Platform представляет таблицу платформ в базе данных.

    Атрибуты:
        id (int): Первичный ключ.
        name (str): Название платформы.
    """
    __tablename__ = 'platform'
    id = Column(Integer, primary_key=True)
    names = Column(String)

class Purchase(Base):
    """
    Класс Purchase представляет таблицу покупок в базе данных.

    Атрибуты:
        id (int): Первичный ключ.
        date (date): Дата покупки.
        amount (int): Количество купленных единиц.
        game_id (int): Внешний ключ, связывающий с таблицей игр.
        employee_id (int): Внешний ключ, связывающий с таблицей сотрудников.
        buyer_id (int): Внешний ключ, связывающий с таблицей покупателей.
    """
    __tablename__ = 'purchase'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    amount = Column(Integer)
    game_id = Column(Integer, ForeignKey('game.id'))
    employee_id = Column(Integer, ForeignKey('employee.id'))
    buyer_id = Column(Integer, ForeignKey('buyer.id'))

