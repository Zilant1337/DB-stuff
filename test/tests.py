import sys
import os

from lib.RandomGenerators import *
from lib import database
from lib import orm
from lib import models
from lib import orm_random

# Параметры базы данных
DATABASE = 'clonedb'
HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
source_database = 'mydb'
target_database = 'clonedb'

# Путь к MySQL и mysqldump
mysqlPath = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
mysqldumpPath = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe"

# Тесты
def test_copy_database_with_foreign_keys():
    try:
        database.copy_database_with_foreign_keys(source_database, target_database)
        print("Тест copy_database_with_foreign_keys прошел успешно.")
    except Exception as e:
        print(f"Тест copy_database_with_foreign_keys провален: {e}")

def test_add_data():
    table = 'game'
    data = {
        'names': 'Test Game',
        'price': 49.99,
        'age_rating': 18,
        'user_rating': 4.5,
        'release_date': '2020-01-01',
        'player_count': 1,
        'language': 'English',
        'stock': 100,
        'platform_id': 1,
        'genre_id': 1,
        'developer_id': 1
    }

    try:
        database.add_data(table, data, DATABASE, HOST, USER, PASSWORD)
        print("Тест add_data прошел успешно.")
    except Exception as e:
        print(f"Тест add_data провален: {e}")

def test_add_random_data():
    table = 'game'
    count = 5

    try:
        database.copy_database_with_foreign_keys(source_database, target_database)
        database.add_random_data(table, count, DATABASE, HOST, USER, PASSWORD)
        print("Тест add_random_data прошел успешно.")
    except Exception as e:
        print(f"Тест add_random_data провален: {e}")

def test_delete_entry():
    table = 'game'
    index = 1

    try:
        database.copy_database_with_foreign_keys(source_database, target_database)
        database.delete_entry(table, index, DATABASE, HOST, USER, PASSWORD)
        print("Тест delete_entry прошел успешно.")
    except Exception as e:
        print(f"Тест delete_entry провален: {e}")

def test_delete_all_entries():
    table = 'game'
    try:
        database.copy_database_with_foreign_keys(source_database, target_database)
        database.delete_all_entries(table, DATABASE, HOST, USER, PASSWORD)
        print("Тест delete_all_entries прошел успешно.")
    except Exception as e:
        print(f"Тест delete_all_entries провален: {e}")

def test_replace_all_entries():
    table = 'game'
    count = 5
    try:
        database.copy_database_with_foreign_keys(source_database, target_database)
        database.replace_all_entries(table, count, DATABASE, HOST, USER, PASSWORD)
        print("Тест replace_all_entries прошел успешно.")
    except Exception as e:
        print(f"Тест replace_all_entries провален: {e}")

session = orm.Session()

def test_orm_add_data():
    try:
        game_data = orm_random.RandomGame(10,10,2)
        game_name=game_data.names
        orm.add_data(session,game_data)

        game = session.query(models.Game).filter_by(names=game_name).first()
        assert game is not None

        print("test_add_data passed")

    finally:
        session.close()

def test_orm_add_random_data():
    try:
        game_count=len(orm.get_all_entries(session,models.Game))
        print(game_count)
        orm.add_random_data(session, models.Game, 5)

        games = session.query(models.Game).all()
        assert len(games) == game_count+5

        print("test_add_random_data passed")

    finally:
        session.close()

def test_orm_delete_entry():
    try:
        game_data = orm_random.RandomGame(10, 10, 2)
        game_name = game_data.names
        orm.add_data(session, game_data)

        game = session.query(models.Game).filter_by(names=game_name).first()
        orm.delete_entry(session, models.Game, game.id)

        game = session.query(models.Game).filter_by(names=game_name).first()
        assert game is None

        print("test_delete_entry passed")

    finally:
        session.close()

def test_orm_delete_all_entries():
    try:
        game_data = orm_random.RandomGame(10,10,2)
        orm.add_data(session, game_data)
        game_data = orm_random.RandomGame(10,10,2)
        orm.add_data(session, game_data)

        orm.delete_all_entries(session, models.Game)

        games = session.query(models.Game).all()
        assert len(games) == 0

        print("test_delete_all_entries passed")

    finally:
        session.close()

def test_orm_replace_all_entries():
    try:
        orm.add_random_data(session, models.Game, 5)

        orm.replace_all_entries(session, models.Game, 10)

        games = session.query(models.Game).all()
        assert len(games) == 10

        print("test_replace_all_entries passed")

    finally:
        session.close()

# Запуск тестов
test_copy_database_with_foreign_keys()
test_add_data()
test_add_random_data()
test_delete_entry()
test_delete_all_entries()
test_replace_all_entries()
test_orm_add_data()
test_orm_add_random_data()
test_orm_delete_entry()
test_orm_delete_all_entries()
test_orm_replace_all_entries()
print("ПАБЕДАААААААААААААААААААААААА")