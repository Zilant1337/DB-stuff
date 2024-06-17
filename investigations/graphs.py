import mysql
import time
from lib.database import *
from lib.orm import *
from lib.RandomGenerators import *
from lib.orm_random import *

def do_generation_graphs(classes, db, file_name, max_rows=1000, step=100):
    """
       Измеряет время генерации данных и строит графики.

       Аргументы:
           classes (list): Список классов для генерации данных.
           db (Database): Объект базы данных для подключения.
           file_name (str): Имя файла для сохранения графика.
           max_rows (int): Максимальное количество строк для генерации.
           step (int): Шаг изменения количества строк.
    """
    row_counts = list(range(step, max_rows + 1, step))
    results = {cls.__name__: [] for cls in classes}

    for cls in classes:
        for row_count in row_counts:
            time_taken = measure_func_time(generate_random_objects, cls, row_count, db)
            results[cls.__name__].append(time_taken)
    labels = [cls.__name__ for cls in classes]
    y_data_list = [results[cls_name] for cls_name in labels]

    plot_graph(
        x_data=row_counts,
        y_data_list=y_data_list,
        labels=labels,
        title='Время генерации данных в зависимости от количества строк',
        xlabel='Количество строк',
        ylabel='Время (секунды)',
        output_file=file_name,
        vector_format=True,
        png_format = True
    )


def do_insert_query_graphs(classes, db, file_name, max_rows=100, step=10):
    """
       Измеряет время выполнения INSERT запросов и строит графики.

       Аргументы:
           classes (list): Список классов для выполнения INSERT запросов.
           db (Database): Объект базы данных для подключения.
           file_name (str): Имя файла для сохранения графика.
           max_rows (int): Максимальное количество строк для вставки.
           step (int): Шаг изменения количества строк.
    """
    row_counts = list(range(step, max_rows + 1, step))
    results = {cls.__name__: [] for cls in classes}
    for cls in classes:
        for row_count in row_counts:
            db.delete_all_entries(cls)
            time_taken = measure_func_time(db.add_random_data, cls, row_count)
            results[cls.__name__].append(time_taken)
    labels = [cls.__name__ for cls in classes]
    select_y_data_list = [results[cls.__name__] for cls in classes]
    plot_graph(
        x_data=row_counts,
        y_data_list=select_y_data_list,
        labels=labels,
        title='Время выполнения разных INSERT запросов',
        xlabel='Количество строк',
        ylabel='Время (секунды)',
        output_file=file_name,
        vector_format=True,
        png_format=True
    )


def do_select_query_graphs(db, cls, select_queries, file_name, max_rows=1000, step=100):
    """
       Измеряет время выполнения SELECT запросов и строит графики.

       Аргументы:
           db (Database): Объект базы данных для подключения.
           cls (Class): Класс для замены всех записей.
           select_queries (list): Список SELECT запросов для выполнения.
           file_name (str): Имя файла для сохранения графика.
           max_rows (int): Максимальное количество строк для генерации.
           step (int): Шаг изменения количества строк.
    """
    row_counts = list(range(step, max_rows + 1, step))
    results = {query: [] for query in select_queries}
    for query in select_queries:
        for row_count in row_counts:
            db.replace_all_entries(cls, row_count)
            time_taken = measure_func_time(db.execute_query, query)
            results[query].append(time_taken)
    labels = [query for query in select_queries]
    insert_y_data_list = [results[query] for query in labels]
    plot_graph(
        x_data=row_counts,
        y_data_list=insert_y_data_list,
        labels=labels,
        title="Время выполнения разных SELECT запросов",
        xlabel='Количество строк',
        ylabel='Время (секунды)',
        output_file=file_name,
        vector_format=True,
        png_format=True
    )


def do_delete_query_graphs(db, cls, condition, file_name, max_rows=1000, step=100):
    """
       Измеряет время выполнения DELETE запросов и строит графики.

       Аргументы:
           db (Database): Объект базы данных для подключения.
           cls (Class): Класс для замены всех записей.
           condition (str): Условие для выполнения DELETE запроса.
           file_name (str): Имя файла для сохранения графика.
           max_rows (int): Максимальное количество строк для генерации.
           step (int): Шаг изменения количества строк.
    """
    row_counts = list(range(step, max_rows + 1, step))
    delete_functions = [
        db.delete_all_entries,
        db.delete_entry,
        db.delete_entry_with_condition
    ]
    results = {function.__name__: [] for function in delete_functions}
    for function in delete_functions:
        for row_count in row_counts:
            db.replace_all_entries(cls, row_count)
            if function is delete_functions[0]:
                time_taken = measure_func_time(function, cls)
                results[function.__name__].append(time_taken)
            elif function is delete_functions[1]:
                time_taken = measure_func_time(function, cls, 1)
                results[function.__name__].append(time_taken)
            elif function is delete_functions[2]:
                time_taken = measure_func_time(function, cls, condition)
                results[function.__name__].append(time_taken)
    labels = [function.__name__ for function in delete_functions]
    delete_y_data_list = [results[function.__name__] for function in delete_functions]
    plot_graph(
        x_data=row_counts,
        y_data_list=delete_y_data_list,
        labels=labels,
        title="Время выполнения разных DELETE запросов",
        xlabel='Количество строк',
        ylabel='Время (секунды)',
        output_file=file_name,
        vector_format=True,
        png_format=True
    )


copy_database_with_foreign_keys('mydb', 'clonedb')

db = Database(host='localhost', user='root', password='root', database='clonedb')
db.connect()

# classes= Employee, Developer, Platform, Genre,
big_classes = Purchase, Game, Buyer
select_queries = [
        "SELECT * FROM game",
        "SELECT * FROM game WHERE game.user_rating > 3",
        "SELECT COUNT(*) FROM game WHERE game.stock > 11000"
    ]
# do_generation_graphs(classes, db, 'smol')
# do_generation_graphs(big_classes, db, 'big')
# do_insert_query_graphs(big_classes, db, "INSERTMEMESY")
# do_select_query_graphs(db, Game, select_queries, "SELECTMEMESY")
# do_delete_query_graphs(db, Game, "language = English", "DELETEMEMESY")
