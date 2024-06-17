from sqlalchemy import Integer, String
import tempfile
from lib.database import *
import os

"""
Этот модуль предоставляет функции для тестирования различных операций с базой данных, включая копирование базы данных, добавление данных, удаление данных, создание резервных копий и восстановление базы данных. Также модуль включает функции для генерации схемы таблицы и измерения времени выполнения функций.

Функции:
- `test_copy_database_with_foreign_keys()`: Тестирует функцию копирования базы данных с учетом внешних ключей.
- `test_add_data()`: Тестирует функцию добавления данных в таблицу.
- `test_add_random_data()`: Тестирует функцию добавления случайных данных в таблицу.
- `test_delete_entry()`: Тестирует функцию удаления записи из таблицы по индексу.
- `test_delete_all_entries()`: Тестирует функцию удаления всех записей из таблицы.
- `test_replace_all_entries()`: Тестирует функцию замены всех записей в таблице случайными данными.
- `test_measure_generate_time()`: Тестирует функцию измерения времени выполнения другой функции.
- `test_generate_schema_for_table_creation()`: Тестирует функцию создания схемы таблицы.
- `test_create_table(database, host, user, password)`: Тестирует функцию создания таблицы в базе данных.
- `test_backup_database(database, host, user, password, backup_dir)`: Тестирует функцию создания резервной копии базы данных.
- `test_restore_database(database, host, user, password, backup_dir)`: Тестирует функцию восстановления базы данных из резервной копии.

Переменные:
- `DATABASE`: Имя базы данных для тестирования.
- `HOST`: Хост базы данных.
- `USER`: Имя пользователя базы данных.
- `PASSWORD`: Пароль пользователя базы данных.
- `source_database`: Имя исходной базы данных для копирования.
- `target_database`: Имя целевой базы данных для копирования.
- `backup_dir`: Директория для хранения временных файлов резервного копирования.
- `mysqlPath`: Путь к исполняемому файлу MySQL.
- `mysqldumpPath`: Путь к исполняемому файлу mysqldump.
"""

# Параметры базы данных
DATABASE = 'clonedb'
HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
source_database = 'mydb'
target_database = 'clonedb'

# Путь к временному файлу, где будет хранится дамп базы данных
backup_dir = tempfile.mkdtemp()

# Путь к MySQL и mysqldump
mysqlPath = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
mysqldumpPath = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe"

def test_copy_database_with_foreign_keys():
    """
    Тестирует функцию copy_database_with_foreign_keys.

    Проверяет успешное копирование базы данных с учетом внешних ключей.
    """
    try:
        copy_database_with_foreign_keys(source_database, target_database)
        print("Тест copy_database_with_foreign_keys прошел успешно.")
    except Exception as e:
        print(f"Тест copy_database_with_foreign_keys провален: {e}")

def test_add_data():
    """
    Тестирует функцию add_data.

    Проверяет успешное добавление данных в таблицу.
    """
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
        add_data(table, data, DATABASE, HOST, USER, PASSWORD)
        print("Тест add_data прошел успешно.")
    except Exception as e:
        print(f"Тест add_data провален: {e}")

def test_add_random_data():
    """
    Тестирует функцию add_random_data.

    Проверяет успешное добавление случайных данных в таблицу.
    """
    table = 'game'
    count = 5

    try:
        copy_database_with_foreign_keys(source_database, target_database)
        add_random_data(table, count, DATABASE, HOST, USER, PASSWORD)
        print("Тест add_random_data прошел успешно.")
    except Exception as e:
        print(f"Тест add_random_data провален: {e}")

def test_delete_entry():
    """
    Тестирует функцию delete_entry.

    Проверяет успешное удаление записи из таблицы по индексу.
    """
    table = 'game'
    index = 1

    try:
        copy_database_with_foreign_keys(source_database, target_database)
        delete_entry(table, index, DATABASE, HOST, USER, PASSWORD)
        print("Тест delete_entry прошел успешно.")
    except Exception as e:
        print(f"Тест delete_entry провален: {e}")

def test_delete_all_entries():
    """
    Тестирует функцию delete_all_entries.

    Проверяет успешное удаление всех записей из таблицы.
    """
    table = 'game'
    try:
        copy_database_with_foreign_keys(source_database, target_database)
        delete_all_entries(table, DATABASE, HOST, USER, PASSWORD)
        print("Тест delete_all_entries прошел успешно.")
    except Exception as e:
        print(f"Тест delete_all_entries провален: {e}")

def test_replace_all_entries():
    """
    Тестирует функцию replace_all_entries.

    Проверяет успешную замену всех записей в таблице случайными данными.
    """
    table = 'game'
    count = 5
    try:
        copy_database_with_foreign_keys(source_database, target_database)
        replace_all_entries(table, count, DATABASE, HOST, USER, PASSWORD)
        print("Тест replace_all_entries прошел успешно.")
    except Exception as e:
        print(f"Тест replace_all_entries провален: {e}")

def test_measure_generate_time():
    """
    Тестирует функцию measure_generate_time.

    Проверяет корректность измерения времени выполнения функции.
    """
    def sample_function(a, b):
        return a + b

    time_taken = measure_generate_time(sample_function, 1, 2)
    print(f"Время выполнения sample_function: {time_taken} секунд")

def test_generate_schema_for_table_creation():
    """
    Тестирует функцию generate_schema_for_table_creation.

    Проверяет корректность создания схемы таблицы.
    """
    columns = {
        'id': Integer,
        'name': String(50)
    }
    metadata = MetaData()
    table = generate_schema_for_table_creation('test_table', columns, metadata)
    print(f"Таблица создана с колонками: {table.columns.keys()}")

def test_create_table(database, host, user, password):
    """
    Тестирует функцию create_table.

    Проверяет успешное создание таблицы в базе данных.
    """
    columns = {
        'id': Integer,
        'name': String(50)
    }
    create_table('test_table', columns, database=database, host=host, user=user, password=password)

def test_backup_database(database, host, user, password, backup_dir):
    """
    Тестирует функцию backup_database.

    Проверяет успешное создание резервной копии базы данных.
    """
    backup_database(database, backup_dir, host=host, user=user, password=password)

def test_restore_database(database, host, user, password, backup_dir):
    """
    Тестирует функцию restore_database.

    Проверяет успешное восстановление базы данных из резервной копии.
    """
    backup_files = os.listdir(backup_dir)
    if backup_files:
        backup_file = os.path.join(backup_dir, backup_files[0])
        restore_database(database, backup_file, host=host, user=user, password=password)

# Запуск тестов
test_copy_database_with_foreign_keys()
test_add_data()
test_add_random_data()
test_delete_entry()
test_delete_all_entries()
test_replace_all_entries()
test_measure_generate_time()
test_generate_schema_for_table_creation()
test_create_table(DATABASE, HOST, USER, PASSWORD)
test_backup_database(DATABASE, HOST, USER, PASSWORD, backup_dir)
test_restore_database(DATABASE, HOST, USER, PASSWORD, backup_dir)

# Очистка временной директории
for root, dirs, files in os.walk(backup_dir):
    for file in files:
        os.remove(os.path.join(root, file))
os.rmdir(backup_dir)
print("Все тесты пройдены")
