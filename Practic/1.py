import sqlite3 as sql

class Database:
    def __init__(self, data_base):
        self.con = sql.connect(data_base)
        self.cur = self.con.cursor()

    # def create_phone_base(self):
    #     self.cur.execute('CREATE TABLE IF NOT EXISTS phone_base(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, number INTEGER)')
    #     self.con.commit() 

    # def insert_phone_base(self, n, a, num):
    #     self.cur.execute("INSERT INTO phone_base(name, age, number) VALUES (?, ?, ?)",(n,a,num))
    #     self.con.commit()
   
    def execute_many(self, dates):
        self.create_table()
        self.cur.executemany("REPLACE INTO phone_base VALUES(?,?,?)", dates)

    def select (self, age, query):
        sql_query ='''SELECT * FROM phone_base ORDER BY age DESC?'''
        self.cur.execute("sql_query, age")
        result = self.cur.fetchall()
        return print('Возраст от большего к меньшему', age, ':', result)

    def close(self):
        self.con.close()

# name=str(input("Введите имя:"))
# age=int(input("Введите возраст:"))
# phone_number=int(input("Введите номер телефона:"))

 

database = Database("phone_number.db")
# database.create_phone_base()
# database.insert_phone_base(name, age, phone_number)
database.select('SELECT * FROM phone_base ORDER BY age DESC')