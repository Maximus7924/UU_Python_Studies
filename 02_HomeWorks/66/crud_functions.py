import sqlite3


def initiate_db():
    connection = sqlite3.connect("Products.db", isolation_level='IMMEDIATE')
    ini_cursor = connection.cursor()
    
    # 1 создаём таблицу с полями и типами данных в полях
    ini_cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
            )
            ''')
    connection.commit()
    connection.close()
    
# в задании нет указаний как именно заполнить базу данными, поэтому решение и функция ниже
def populate_db():
    connection = sqlite3.connect("Products.db", isolation_level='IMMEDIATE')
    pop_cursor = connection.cursor()
    
    # 2 будем заполнять базу и надеемся что ВСТАВИТЬ ИЛИ ИГНОРИТЬ отработает как надо
    for prod_item in range(4):
        prod_item += 1
        pop_cursor.execute("INSERT OR IGNORE INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)",
                           (f"{prod_item}",
                            f"Продукт {prod_item}",
                            f"Описание {prod_item}",
                            f"{100 * prod_item}"))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("Products.db", isolation_level='IMMEDIATE')
    get_cursor = connection.cursor()
    
    # 3 выборка "продуктов" из базы которую создали и наполнили
    get_cursor.execute("SELECT * FROM Products")
    get_products = get_cursor.fetchall() # в задании указано "возвращает ВСЕ записи" поэтому "фетч ол"
    connection.commit()
    connection.close()
    return  get_products

initiate_db()
populate_db()

# all_products = get_all_products()
# # первый вызов
# print(all_products)
# # второй вызов когда базу уже создали и заполнили
# print(f"{all_products[0][1]}\n{all_products[1][1]}\n{all_products[2][1]}\n{all_products[3][1]}\n")
