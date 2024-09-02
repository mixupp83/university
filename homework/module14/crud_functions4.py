import sqlite3


def initiate_db():
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products


def insert_product(title, description, price):
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', (title, description, price))

    conn.commit()
    conn.close()


# Вызов функции initiate_db перед любыми операциями с базой данных
initiate_db()

# Пример вставки данных
insert_product('Product1', 'Описание 1', 100)
insert_product('Product2', 'Описание 2', 200)
insert_product('Product3', 'Описание 3', 300)
insert_product('Product4', 'Описание 4', 400)