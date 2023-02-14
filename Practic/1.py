import sqlite3 as sql

name=str(input("Введите имя:"))
age=int(input("Введите возраст:"))
phone_number=int(input("Введите номер телефона:"))


class Database:
    def __init__(self, data_base):
        self.con = sql.connect(data_base)
        self.cur = self.con.cursor()

    def create_phone_base(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS phone_base(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, number INTEGER)')
        self.con.commit() 

    def insert_phone_base(self, name, age, phone_number):
        self.cur.execute("INSERT INTO phone_base(name, age, number) VALUES (?, ?, ?)", (name, age, phone_number))
        self.con.commit()

    def select (self, query):
        self.cur.execute('SELECT * FROM phone_base ORDER BY age DESC')
        result = self.cur.fetchall()
        return print('Возраст от большего к меньшему', result)

    def close(self):
        self.con.close()

 

database = Database("phone_number.db")
# database.create_phone_base()
database.insert_phone_base(name, age, phone_number)
database.select('SELECT * FROM phone_base ORDER BY age DESC')