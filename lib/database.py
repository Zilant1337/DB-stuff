import datetime
import mysql.connector
import subprocess
import timeit
import itertools
import matplotlib.pyplot as plt
from lib import RandomGenerators
from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.ext.declarative import declarative_base

mysqlPath = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
mysqldumpPath = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe"

Base = declarative_base()

def copy_database_with_foreign_keys(source_database, target_database, host='localhost', user='root', password='root'):
    """
    Копирует базу данных MySQL вместе с ее внешними ключами из исходной базы данных в целевую.

    Аргументы:
        source_database (str): Имя исходной базы данных, которую нужно скопировать.
        target_database (str): Имя целевой базы данных, в которую будут скопированы данные.
        host (str, optional): Имя хоста сервера MySQL. По умолчанию 'localhost'.
        user (str, optional): Имя пользователя MySQL. По умолчанию 'root'.
        password (str, optional): Пароль MySQL. По умолчанию 'root'.

    Исключения:
        subprocess.CalledProcessError: В случае ошибки во время процесса дампа или восстановления базы данных.
    """
    global mysqldumpPath, mysqlPath
    try:
        dump_cmd = [
            mysqldumpPath,
            '--single-transaction',
            '-h', host,
            '-u', user,
            '-p' + password,
            source_database,
            '>', f'{source_database}.sql'
        ]

        subprocess.run(dump_cmd, shell=True, check=True)

        restore_cmd = [
            mysqlPath,
            '-h', host,
            '-u', user,
            '-p' + password,
            target_database,
            '<', f'{source_database}.sql'
        ]

        subprocess.run(restore_cmd, shell=True, check=True)

        print(f"База данных '{source_database}' успешно скопирована в '{target_database}'.")

    except subprocess.CalledProcessError as e:
        print(f"Ошибка: {e}")


def add_data(table, data, database='clonedb', host='localhost', user='root', password='root'):
    """
    Добавляет запись в указанную таблицу базы данных MySQL.

    Аргументы:
        table (str): Имя таблицы, в которую будут добавлены данные.
        data (dict): Словарь, содержащий имена столбцов и значения для новой записи.
        database (str, optional): Имя базы данных. По умолчанию 'clonedb'.
        host (str, optional): Имя хоста сервера MySQL. По умолчанию 'localhost'.
        user (str, optional): Имя пользователя MySQL. По умолчанию 'root'.
        password (str, optional): Пароль MySQL. По умолчанию 'root'.

    Исключения:
        mysql.connector.Error: В случае ошибки при добавлении данных в таблицу.
    """
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    try:
        columns = ", ".join(data.keys())
        values = ", ".join(f"'{value}'" for value in data.values())
        query = f'INSERT INTO {table}({columns}) VALUES({values})'

        cursor.execute(query)
        conn.commit()
        print("Запись успешно добавлена")
    except mysql.connector.Error as err:
        print(f"Ошибка: {err}")
    finally:
        cursor.close()
        conn.close()


def add_random_data(table, count, database='clonedb', host='localhost', user='root', password='root'):
    """
    Добавляет несколько случайных записей в указанную таблицу базы данных MySQL.

    Аргументы:
        table (str): Имя таблицы, в которую будут добавлены случайные данные.
        count (int): Количество случайных записей, которые нужно добавить.
        database (str, optional): Имя базы данных. По умолчанию 'clonedb'.
        host (str, optional): Имя хоста сервера MySQL. По умолчанию 'localhost'.
        user (str, optional): Имя пользователя MySQL. По умолчанию 'root'.
        password (str, optional): Пароль MySQL. По умолчанию 'root'.
    """
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    for i in range(count):
        if table == "purchase":
            cursor.execute(f"SELECT COUNT(*) FROM {database}.game")
            gameIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {database}.employee")
            employeeIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {database}.buyer")
            buyerIdLimit = cursor.fetchone()[0]
            data = RandomGenerators.RandomPurchase(gameIdLimit, employeeIdLimit, buyerIdLimit)
            add_data(table, data)
        if table == "employee":
            data = RandomGenerators.RandomEmployee()
            add_data(table, data)
        if table == "buyer":
            cursor.execute(f"SELECT COUNT(*) FROM {database}.platform")
            platformIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {database}.genre")
            genreIdLimit = cursor.fetchone()[0]
            data = RandomGenerators.RandomBuyer(platformIdLimit, genreIdLimit)
            add_data(table, data)
        if table == "game":
            cursor.execute(f"SELECT COUNT(*) FROM {database}.platform")
            platformIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {database}.genre")
            genreIdLimit = cursor.fetchone()[0]
            cursor.execute(f"SELECT COUNT(*) FROM {database}.developer")
            developerIdLimit = cursor.fetchone()[0]
            data = RandomGenerators.RandomGame(platformIdLimit, genreIdLimit, developerIdLimit)
            add_data(table, data)
        if table == "platform":
            data = RandomGenerators.RandomPlatform()
            add_data(table, data)
        if table == "developer":
            data = RandomGenerators.RandomDeveloper()
            add_data(table, data)
        if table == "genre":
            data = RandomGenerators.RandomGenre()
            add_data(table,data)
def delete_entry(table, index, database='clonedb', host='localhost', user='root', password='root'):
    """
    Удаляет конкретную запись из указанной таблицы базы данных MySQL.

    Аргументы:
        table (str): Имя таблицы, из которой будет удалена запись.
        index (int): Индекс (id) записи, которую нужно удалить.
        database (str, optional): Имя базы данных. По умолчанию 'clonedb'.
        host (str, optional): Имя хоста сервера MySQL. По умолчанию 'localhost'.
        user (str, optional): Имя пользователя MySQL. По умолчанию 'root'.
        password (str, optional): Пароль MySQL. По умолчанию 'root'.

    Исключения:
        mysql.connector.Error: В случае ошибки при удалении записи из таблицы.
    """
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    try:
        cursor.execute(f"DELETE FROM {table} WHERE id= {index}")
        conn.commit()
        print(f"Запись успешно удалена")
    except mysql.connector.Error as err:
        print(f"Ошибка: {err}")
    finally:
        cursor.close()
        conn.close()


def delete_all_entries(table, database='clonedb', host='localhost', user='root', password='root'):
    """
    Удаляет все записи из указанной таблицы базы данных MySQL.

    Аргументы:
        table (str): Имя таблицы, из которой будут удалены все записи.
        database (str, optional): Имя базы данных. По умолчанию 'clonedb'.
        host (str, optional): Имя хоста сервера MySQL. По умолчанию 'localhost'.
        user (str, optional): Имя пользователя MySQL. По умолчанию 'root'.
        password (str, optional): Пароль MySQL. По умолчанию 'root'.

    Исключения:
        mysql.connector.Error: В случае ошибки при удалении всех записей из таблицы.
    """
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    try:
        cursor.execute(f"TRUNCATE TABLE {table}")
        conn.commit()
        print(f"Все записи в {database}.{table} успешно удалены")
    except mysql.connector.Error as err:
        print(f"Ошибка: {err}")
    finally:
        cursor.close()
        conn.close()


def replace_all_entries(table, count, database='clonedb', host='localhost', user='root', password='root'):
    """
    Заменяет все записи в указанной таблице новыми случайными данными в базе данных MySQL.

    Аргументы:
        table (str): Имя таблицы, записи в которой будут заменены.
        count (int): Количество новых случайных записей, которые нужно добавить.
        database (str, optional): Имя базы данных. По умолчанию 'clonedb'.
        host (str, optional): Имя хоста сервера MySQL. По умолчанию 'localhost'.
        user (str, optional): Имя пользователя MySQL. По умолчанию 'root'.
        password (str, optional): Пароль MySQL. По умолчанию 'root'.

    Исключения:
        mysql.connector.Error: В случае ошибки при замене записей в таблице.
    """
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    try:
        cursor.execute(f"TRUNCATE TABLE {table}")
    except mysql.connector.Error as err:
        print(f"Error:{err}\n Deleting purchase and trying again...")
        cursor.execute(f"TRUNCATE TABLE purchase")
    conn.commit()
    try:
        add_random_data(table, count, database, host, user, password)
        print(f"Replaced all data in {database}.{table} with {count} random entries successfully")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        cursor.close()
        conn.close()
def measure_func_time(func, *args):
    """
    Измеряет время выполнения заданной функции.

    Аргументы:
        func (callable): Функция для измерения времени.
        *args: Аргументы для функции.

    Возвращает:
        float: Время выполнения функции в секундах.
    """
    wrapped = lambda: func(*args)
    time_taken = timeit.timeit(wrapped, number=1)
    return time_taken

def generate_schema_for_table_creation(table_name, columns, metadata):
    """
    Аргументы:
        table_name (str): Имя создаваемой таблицы.
        columns (dict): Словарь, где ключами являются имена столбцов, а значениями - их типы в формате SQLAlchemy.
    Возвращает:
        table: Объект таблицы SQLAlchemy.
    """
    metadata1 = metadata
    table = Table(
        table_name,
        metadata1,
        *(Column(col_name, col_type) for col_name, col_type in columns.items())
    )
    return table

def create_table(table_name, columns, database='clonedb', host='localhost', user='root', password='root'):
    """
    Создает новую таблицу в указанной базе данных MySQL.

    Аргументы:

        table_name (str): Имя создаваемой таблицы.
        columns (dict): Словарь, где ключами являются имена столбцов, а значениями - их типы в формате SQLAlchemy.
        database (str, optional): Имя базы данных. По умолчанию 'clonedb'.
        host (str, optional): Хост сервера MySQL. По умолчанию 'localhost'.
        user (str, optional): Пользователь MySQL. По умолчанию 'root'.
        password (str, optional): Пароль MySQL. По умолчанию 'root'.
    """
    DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
    engine = create_engine(DATABASE_URL, echo=True)
    metadata = MetaData()
    table = generate_schema_for_table_creation(table_name, columns, metadata)
    try:
        print(f"Creating table {table_name}: ", end='')
        table.create(engine)
        print("OK")
    except Exception as e:
        print(f"Failed to create table: {e}")

def backup_database(database, backup_path, host='localhost', user='root', password='root'):
    """
    Создает резервную копию указанной базы данных MySQL.

    Аргументы:
        database (str): Имя базы данных для резервного копирования.
        backup_path (str): Директория, в которую будет сохранен файл резервной копии.
        host (str, optional): Хост сервера MySQL. По умолчанию 'localhost'.
        user (str, optional): Пользователь MySQL. По умолчанию 'root'.
        password (str, optional): Пароль MySQL. По умолчанию 'root'.
    """
    global mysqldumpPath
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_file = f"{backup_path}\\{database}_backup_{timestamp}.sql"

    dump_cmd = [
        mysqldumpPath,
        '--single-transaction',
        '-h', host,
        '-u', user,
        f"-p{password}",
        database,
        '-r', backup_file
    ]

    try:
        print(f"Creating backup for database '{database}'...")
        subprocess.run(dump_cmd, check=True)
        print(f"Backup created successfully at '{backup_file}'")
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e}")


def restore_database(database, backup_file, host='localhost', user='root', password='root'):
    """
    Восстанавливает указанную базу данных MySQL из резервной копии.

    Аргументы:
        database (str): Имя базы данных для восстановления.
        backup_file (str): Путь к файлу резервной копии.
        host (str, optional): Хост сервера MySQL. По умолчанию 'localhost'.
        user (str, optional): Пользователь MySQL. По умолчанию 'root'.
        password (str, optional): Пароль MySQL. По умолчанию 'root'.
    """
    global mysqlPath

    restore_cmd = [
        mysqlPath,
        '-h', host,
        '-u', user,
        f"-p{password}",
        database
    ]

    try:
        print(f"Restoring database '{database}' from backup '{backup_file}'...")
        with open(backup_file, 'rb') as f:
            subprocess.run(restore_cmd, stdin=f, check=True)
        print(f"Database '{database}' restored successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during restore: {e}")


def plot_graph(x_data, y_data_list, labels, title, xlabel, ylabel, output_file, vector_format=False, png_format = False):
    """
    Построение и сохранение графика.

    Параметры:
        x_data (list): Данные для оси X.
        y_data_list (list of lists): Список рядов данных для оси Y.
        labels (list): Список меток для каждого ряда данных.
        title (str): Название графика.
        xlabel (str): Подпись оси X.
        ylabel (str): Подпись оси Y.
        output_file (str): Имя файла для сохранения графика.
        vector_format (bool): Сохранить как векторное изображение, если True. В противном случае сохранить как растровое изображение.
    """
    colors = itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
    linestyles = itertools.cycle(['-', '--', '-.', ':'])
    markers = itertools.cycle(['o', 's', '^', 'D', 'v', '<', '>', 'p', '*'])

    plt.figure()
    for y_data, label in zip(y_data_list, labels):
        color = next(colors)
        linestyle = next(linestyles)
        marker = next(markers) if len(x_data) < 10 else ''
        plt.plot(x_data, y_data, color=color, linestyle=linestyle, marker=marker, label=label)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
    if vector_format:
        plt.savefig(output_file, format='svg')
    if png_format:
        plt.savefig(output_file, format='png')

    plt.close()