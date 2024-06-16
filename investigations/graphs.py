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





copy_database_with_foreign_keys('mydb', 'clonedb')

db = Database(host='localhost', user='root', password='root', database='clonedb')
db.connect()

classes= Employee, Developer, Platform, Genre,
big_classes = Purchase, Game, Buyer
do_generation_graphs(classes,db, 'smol')
do_generation_graphs(big_classes,db, 'big')
