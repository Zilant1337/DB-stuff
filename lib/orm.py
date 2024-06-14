import random
import mysql.connector
from lib import models
from lib import orm_random

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database!")
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the database.")
    def get_tables(self):
        self.cursor.execute("SHOW TABLES")
        tables = [table[0] for table in self.cursor.fetchall()]
        return tables

class Model:
    def __init__(self, db):
        self.db = db

    def save(self):
        column_names = list(self.__dict__.keys())[1:]
        values_names = list(self.__dict__.values())[1:]
        columns = ', '.join(column_names)
        values = ', '.join([f"'{v}'" if isinstance(v, str) else str(v) for v in values_names])
        query = f"INSERT INTO {self.__class__.__name__.lower()} ({columns}) VALUES ({values})"
        print (query)
        try:
            self.db.cursor.execute(query)
            self.db.connection.commit()
            print("Record saved successfully!")
        except mysql.connector.Error as e:
            print(f"Error saving record: {e}")

    @classmethod
    def create(cls, db, **kwargs):
        instance = cls(db, **kwargs)
        instance.save()
        return instance
    @classmethod
    def create_table(cls, db):
        table_name = cls.__name__.lower()
        if table_name not in db.get_tables():
            table_query = f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY"
            for field_name, field in cls._fields.items():
                field_query = f", {field_name} {field.field_type}"
                if (field.field_type == 'VARCHAR'):
                    field_query += f" ({field.varchar_length})"
                if field.primary_key:
                    field_query += " PRIMARY KEY"
                elif field.foreign_key:
                    field_query += f" REFERENCES {field.foreign_key}"
                elif field.many_to_many:
                    field_query += f" FOREIGN KEY REFERENCES {field.many_to_many}"
                elif field.min_value is not None and field.max_value is not None:
                    field_query += f" CHECK ({field_name} BETWEEN {field.min_value} AND {field.max_value})"
                # elif field.words_count:
                #     field_query += f" CHECK (LENGTH({field_name}) - LENGTH(REPLACE({field_name}, ' ', '')) = {field.words_count - 1})"
                table_query += field_query
            table_query += ")"
            print(table_query)
            try:
                db.cursor.execute(table_query)
                db.connection.commit()
                print(f"{table_name} table created successfully!")
            except mysql.connector.Error as e:
                print(f"Error creating {table_name} table: {e}")

class Field:
    def __init__(self, field_type,varchar_length=255, primary_key=False, foreign_key=None, many_to_many=None, min_value=None, max_value=None, words_count=None):
        self.field_type = field_type
        self.primary_key = primary_key
        self.foreign_key = foreign_key
        self.many_to_many = many_to_many
        self.min_value = min_value
        self.max_value = max_value
        self.words_count = words_count
        self.varchar_length = varchar_length

class IntegerField(Field):
    def __init__(self, **kwargs):
        super().__init__('INT', **kwargs)
class FloatField(Field):
    def __init__(self,**kwargs):
        super().__init__(field_type='FLOAT',**kwargs)
class DateField(Field):
    def __init__(self, **kwargs):
        super().__init__(field_type='DATE', **kwargs)
class CharField(Field):
    def __init__(self, **kwargs):
        super().__init__('VARCHAR', **kwargs)

class ModelMeta(type):
    def __new__(cls, name, bases, dct):
        fields = {}
        for attr_name, attr_value in dct.items():
            if isinstance(attr_value, Field):
                fields[attr_name] = attr_value
        dct['_fields'] = fields
        return super().__new__(cls, name, bases, dct)

class ModelBase(Model, metaclass=ModelMeta):
    pass

class User(ModelBase):
    names = CharField(words_count=2)
    age = IntegerField(min_value=1, max_value=120)

    def __init__(self, db, **kwargs):
        super().__init__(db)
        for attr_name, attr_value in kwargs.items():
            setattr(self, attr_name, attr_value)


class Employee(ModelBase):
    names=CharField(words_count=1)
    birth_date=DateField()
    def __init__(self, db, **kwargs):
        super().__init__(db)
        for attr_name, attr_value in kwargs.items():
            setattr(self, attr_name, attr_value)