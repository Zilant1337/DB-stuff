import mysql.connector
import re
from lib.database import *

class Database:
    def __init__(self, host, user, password, database):
        """
        Класс для работы с базой данных MySQL.

        Аргументы:
            host (str): Адрес хоста базы данных.
            user (str): Имя пользователя.
            password (str): Пароль пользователя.
            database (str): Имя базы данных.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        """Устанавливает соединение с базой данных."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Подключено к базе данных!")
        except mysql.connector.Error as e:
            print(f"Ошибка: {e}")

    def disconnect(self):
        """Закрывает соединение с базой данных."""
        if self.connection:
            self.connection.close()
            print("Отключено от базы данных.")

    def get_tables(self):
        """
        Получает список таблиц в базе данных.

        Возвращает:
            list: Список имен таблиц.
        """
        self.cursor.execute("SHOW TABLES")
        tables = [table[0] for table in self.cursor.fetchall()]
        return tables

    def delete_all_entries(self, cls):
        """
        Удаляет все записи из таблицы.

        Аргументы:
            cls (class): Класс модели, записи которой необходимо удалить.
        """
        delete_all_entries(cls.__name__.lower(), self.database, self.host, self.user, self.password)

    def add_random_data(self, cls, count):
        """
        Добавляет случайные данные в таблицу.

        Аргументы:
            cls (class): Класс модели, в таблицу которой нужно добавить данные.
            count (int): Количество записей для добавления.
        """
        add_random_data(cls.__name__.lower(), count, self.database, self.host, self.user, self.password)

    def delete_entry(self, cls, id):
        """
        Удаляет запись из таблицы по ID.

        Аргументы:
            cls (class): Класс модели, из таблицы которой нужно удалить запись.
            id (int): ID записи для удаления.
        """
        delete_entry(cls.__name__.lower(), id, self.database, self.host, self.user, self.password)

    def delete_entry_with_condition(self, cls, condition):
        """
        Удаляет записи из таблицы по условию.

        Аргументы:
            cls (class): Класс модели, из таблицы которой нужно удалить записи.
            condition (str): Условие для удаления записей.
        """
        delete_entry_with_condition(cls.__name__.lower(), condition, self.database, self.host, self.user, self.password)

    def replace_all_entries(self, cls, count):
        """
        Заменяет все записи в таблице случайными данными.

        Аргументы:
            cls (class): Класс модели, в таблице которой нужно заменить данные.
            count (int): Количество записей для замены.
        """
        replace_all_entries(cls.__name__.lower(), count, self.database, self.host, self.user, self.password)

    def execute_query(self, query):
        """
        Выполняет произвольный SQL-запрос.

        Аргументы:
            query (str): SQL-запрос для выполнения.
        """
        execute_query(query, self.database, self.host, self.user, self.password)

    def get_all_entries(self, cls):
        """
        Получает все записи из таблицы.

        Аргументы:
            cls (class): Класс модели, записи которой необходимо получить.

        Возвращает:
            list: Список объектов модели.
        """
        entries = get_all_entries(cls.__name__.lower(), self.database, self.host, self.user, self.password)
        entry_objects = []
        for entry in entries:
            print(entry)
            object = cls.create(self, **entry)
            object.id = entry["id"]
            entry_objects.append(object)

        return entry_objects

    def get_entry(self, cls, id):
        """
        Получает запись из таблицы по ID.

        Аргументы:
            cls (class): Класс модели, запись которой необходимо получить.
            id (int): ID записи для получения.

        Возвращает:
            object: Объект модели.
        """
        entry = get_entry(cls.__name__.lower(), id, self.database, self.host, self.user, self.password)
        print(entry)
        object = cls.create(self, **entry)
        object.id = id
        return object

class Field:
    def __init__(self, field_type, varchar_length=255, primary_key=False, foreign_key=None, min_value=None, max_value=None):
        """
        Базовый класс для описания полей в модели.

        Аргументы:
            field_type (str): Тип поля (например, 'INT', 'VARCHAR', 'DATE' и т. д.).
            varchar_length (int, optional): Длина VARCHAR поля. По умолчанию 255.
            primary_key (bool, optional): Является ли поле первичным ключом. По умолчанию False.
            foreign_key (tuple, optional): Если поле внешний ключ, то кортеж ('связанная_таблица', 'связанное_поле').
            min_value (int/float, optional): Минимальное значение для числового поля.
            max_value (int/float, optional): Максимальное значение для числового поля.
        """
        self.field_type = field_type
        self.primary_key = primary_key
        self.foreign_key = foreign_key
        self.min_value = min_value
        self.max_value = max_value
        self.varchar_length = varchar_length

class IntegerField(Field):
    def __init__(self, **kwargs):
        """
        Целочисленное поле.

        Аргументы:
            **kwargs: Параметры поля (см. Field).
        """
        super().__init__('INT', **kwargs)

class FloatField(Field):
    def __init__(self, **kwargs):
        """
        Поле с плавающей точкой.

        Аргументы:
            **kwargs: Параметры поля (см. Field).
        """
        super().__init__(field_type='FLOAT', **kwargs)

class DateField(Field):
    def __init__(self, **kwargs):
        """
        Поле даты.

        Аргументы:
            **kwargs: Параметры поля (см. Field).
        """
        super().__init__(field_type='DATE', **kwargs)

class CharField(Field):
    def __init__(self, **kwargs):
        """
        Символьное поле.

        Аргументы:
            **kwargs: Параметры поля (см. Field).
        """
        super().__init__('VARCHAR', **kwargs)

class ManyToManyField(Field):
    def __init__(self, related_model):
        """
        Многие ко многим отношение.

        Аргументы:
            related_model (str): Имя связанной модели.
        """
        super().__init__(field_type='MANY_TO_MANY')
        self.related_model = related_model

class Model:
    def __init__(self, db):
        """
        Базовый класс для моделей.

        Аргументы:
            db (Database): Объект базы данных.
        """
        self.db = db

    def save(self):
        """Сохраняет объект в базу данных."""
        if(self.id is not None):
            delete_entry(self.__class__.__name__.lower(),self.id,self.db.database,self.db.host,self.db.user,self.db.password)
            self.id = None
        column_names = list(self.__dict__.keys())[1:]  # исключаем 'db'
        values_names = list(self.__dict__.values())[1:]  # исключаем 'db'
        for i in range(len(column_names)):
            if column_names[i] == 'id':
                column_names.pop(i)
                values_names.pop(i)

        columns = ', '.join(column_names)
        values = ', '.join([f"'{v}'" if isinstance(v, str) else str(v) for v in values_names])
        query = f"INSERT INTO {self.__class__.__name__.lower()} ({columns}) VALUES ({values})"
        print(query)
        try:
            self.db.cursor.execute(query)
            self.db.connection.commit()
            self.id = self.db.cursor.lastrowid  # присваиваем ID, сгенерированный БД
            print("Record saved successfully!")
        except mysql.connector.Error as e:
            print(f"Error saving record: {e}")

    @classmethod
    def create(cls, db, **kwargs):
        """
        Создает новый объект модели.

        Аргументы:
            db (Database): Объект базы данных.
            **kwargs: Поля модели.

        Возвращает:
            Model: Созданный объект модели.
        """
        instance = cls(db, **kwargs)
        return instance
    @classmethod
    def create_and_save(cls, db, **kwargs):
        """
        Создает новый объект модели и сохраняет его в базу данных.

        Аргументы:
            db (Database): Объект базы данных.
            **kwargs: Поля модели.

        Возвращает:
            Model: Созданный объект модели.
        """
        instance = cls(db, **kwargs)
        instance.save()
        return instance

    @classmethod
    def create_table(cls, db):
        """
        Создает таблицу для модели в базе данных.

        Аргументы:
            db (Database): Объект базы данных.
        """
        table_name = cls.__name__.lower()
        if table_name not in db.get_tables():
            table_query = f"CREATE TABLE {table_name} (\nid INT AUTO_INCREMENT PRIMARY KEY"
            for field_name, field in cls._fields.items():
                if isinstance(field, ManyToManyField):
                    continue  # Обрабатываем поля многие ко многим отдельно
                field_query = f",\n{field_name} {field.field_type}"
                if field.field_type == 'VARCHAR':
                    field_query += f" ({field.varchar_length})"
                if field.primary_key:
                    field_query += " PRIMARY KEY"
                elif field.min_value is not None:
                    field_query += f" CHECK ({field_name} >= {field.min_value}"
                    if field.max_value is not None:
                        field_query += f" AND {field_name} <= {field.max_value}"
                    field_query += ")"
                elif field.min_value is None and field.max_value is not None:
                    field_query += f" CHECK ({field_name} <= {field.max_value})"
                elif field.foreign_key:
                    field_query += f",\nFOREIGN KEY ({field_name}) REFERENCES {field.foreign_key[0].lower()}({field.foreign_key[1]})"
                table_query += field_query
            table_query += ")"
            print(table_query)
            try:
                db.cursor.execute(table_query)
                db.connection.commit()
                print(f"Таблица {table_name} успешно создана!")
            except mysql.connector.Error as e:
                print(f"Ошибка: {e}")

        # Создание объединяющей таблицы для связи многие ко многим
        for field_name, field in cls._fields.items():
            if isinstance(field, ManyToManyField):
                related_table_name = field.related_model.lower()
                join_table_name = f"{table_name}_{related_table_name}"
                if join_table_name not in db.get_tables():
                    join_table_query = f"CREATE TABLE {join_table_name} (\n"
                    join_table_query += f"{table_name}_id INT,\n"
                    join_table_query += f"{related_table_name}_id INT,\n"
                    join_table_query += f"FOREIGN KEY ({table_name}_id) REFERENCES {table_name}(id),\n"
                    join_table_query += f"FOREIGN KEY ({related_table_name}_id) REFERENCES {related_table_name}(id)"
                    join_table_query += ")"
                    print(join_table_query)
                    try:
                        db.cursor.execute(join_table_query)
                        db.connection.commit()
                        print(f"{join_table_name} таблица соединения создана!")
                    except mysql.connector.Error as e:
                        print(f"Ошибка: {e}")

    def add_related(self, related_obj):
        """
        Добавляет связанный объект.

        Аргументы:
            related_obj (Model): Связанный объект.
        """
        table_name = self.__class__.__name__.lower()
        related_table_name = related_obj.__class__.__name__.lower()
        join_table_name = f"{table_name}_{related_table_name}"
        query = f"INSERT INTO {join_table_name} ({table_name}_id, {related_table_name}_id) VALUES ({self.id}, {related_obj.id})"
        print(query)
        try:
            self.db.cursor.execute(query)
            self.db.connection.commit()
            print(f"Отношение многие ко многим {table_name} и {related_table_name} создано")
        except mysql.connector.Error as e:
            print(f"Ошибка: {e}")

class ModelMeta(type):
    def __new__(cls, name, bases, dct):
        fields = {}
        # Проверяем явно определенные поля в словаре класса
        for attr_name, attr_value in dct.items():
            if isinstance(attr_value, Field):
                fields[attr_name] = attr_value

        # Если явных полей не найдено, выполняем парсинг документации
        if not fields:
            docstring = dct.get('__doc__', '')
            if docstring:
                lines = docstring.strip().split('\n')
                for line in lines:
                    line = line.strip()
                    match = re.match(r'(\w+):\s*(\w+)(?:\((.*)\))?', line)
                    if match:
                        field_name, field_type, params = match.groups()
                        field_type = field_type.lower()
                        if field_type == 'charfield':
                            max_length = 255
                            if params:
                                max_length = int(params.split('=')[1])
                            fields[field_name] = CharField(varchar_length=max_length)
                        elif field_type == 'integerfield':
                            min_value, max_value = None, None
                            if params:
                                for param in params.split(','):
                                    k, v = param.split('=')
                                    if k.strip() == 'min_value':
                                        min_value = int(v)
                                    elif k.strip() == 'max_value':
                                        max_value = int(v)
                            fields[field_name] = IntegerField(min_value=min_value, max_value=max_value)
                        elif field_type == 'floatfield':
                            min_value, max_value = None, None
                            if params:
                                for param in params.split(','):
                                    k, v = param.split('=')
                                    if k.strip() == 'min_value':
                                        min_value = float(v)
                                    elif k.strip() == 'max_value':
                                        max_value = float(v)
                            fields[field_name] = FloatField(min_value=min_value, max_value=max_value)
                        elif field_type == 'datefield':
                            fields[field_name] = DateField()
                        elif field_type == 'manytomanyfield':
                            fields[field_name] = ManyToManyField(params.strip())
        dct['_fields'] = fields
        return super().__new__(cls, name, bases, dct)

class ModelBase(Model, metaclass=ModelMeta):
    def __init__(self, db, **kwargs):
        super().__init__(db)
        for attr_name, attr_value in kwargs.items():
            setattr(self, attr_name, attr_value)
        self.id = None

# Оставшиеся классы с документациями

class Employee(ModelBase):
    """
    Модель работника.

    Поля:
        names (CharField): Имя сотрудника.
        birth_date (DateField): Дата рождения сотрудника.
    """
    names = CharField(varchar_length=45)
    birth_date = DateField()

class Developer(ModelBase):
    """
    Модель разработчика.

    Поля:
        names (CharField): Имя разработчика.
        user_rating (FloatField): Рейтинг пользователя разработчика.
    """
    names = CharField(varchar_length=45)
    user_rating = FloatField(min_value=0, max_value=5)

class Buyer(ModelBase):
    """
    Модель покупателя.

    Поля:
        names (CharField): Имя покупателя.
        password (CharField): Пароль покупателя.
        birth_date (DateField): Дата рождения покупателя.
        Platform_id (IntegerField): ID платформы (внешний ключ).
        Genre_id (IntegerField): ID жанра (внешний ключ).
        boughtgames (IntegerField): Количество купленных игр.
    """
    names = CharField(varchar_length=300)
    password = CharField(varchar_length=45)
    birth_date = DateField()
    Platform_id = IntegerField(min_value=1, foreign_key=('platform', 'id'))
    Genre_id = IntegerField(min_value=1, foreign_key=('genre', 'id'))
    boughtgames = IntegerField(min_value=0)

class Platform(ModelBase):
    """
    Модель игровой платформы.

    Поля:
        names (CharField): Имя платформы.
    """
    names = CharField(varchar_length=45)

class Genre(ModelBase):
    """
    Модель игрового жанра.

    Поля:
        names (CharField): Имя жанра.
    """
    names = CharField(varchar_length=45)

class Purchase(ModelBase):
    """
    Модель покупки.

    Поля:
        dates (DateField): Дата покупки.
        amount (IntegerField): Количество купленных единиц.
        Game_id (IntegerField): ID игры (внешний ключ).
        Employee_id (IntegerField): ID сотрудника (внешний ключ).
        Buyer_id (IntegerField): ID покупателя (внешний ключ).
    """
    dates = DateField()
    amount = IntegerField(min_value=0)
    Game_id = IntegerField(min_value=1, foreign_key=('game', 'id'))
    Employee_id = IntegerField(min_value=1, foreign_key=('employee', 'id'))
    Buyer_id = IntegerField(min_value=1, foreign_key=('buyer', 'id'))

class Game(ModelBase):
    """
    Модель игры.

    Поля:
        names (CharField): Название игры.
        price (FloatField): Цена игры.
        age_rating (IntegerField): Возрастной рейтинг игры.
        user_rating (FloatField): Рейтинг пользователей игры.
        release_date (DateField): Дата выпуска игры.
        player_count (IntegerField): Количество игроков.
        language (CharField): Язык игры.
        stock (IntegerField): Наличие на складе.
        Platform_id (IntegerField): ID платформы (внешний ключ).
        Genre_id (IntegerField): ID жанра (внешний ключ).
        Developer_id (IntegerField): ID разработчика (внешний ключ).
    """
    names = CharField(varchar_length=45)
    price = FloatField(min_value=0)
    age_rating = IntegerField(min_value=0)
    user_rating = FloatField(min_value=0, max_value=5)
    release_date = DateField()
    player_count = IntegerField(min_value=1)
    language = CharField(varchar_length=45)
    stock = IntegerField(min_value=0)
    Platform_id = IntegerField(min_value=1, foreign_key=('platform', 'id'))
    Genre_id = IntegerField(min_value=1, foreign_key=('genre', 'id'))
    Developer_id = IntegerField(min_value=1, foreign_key=('developer', 'id'))