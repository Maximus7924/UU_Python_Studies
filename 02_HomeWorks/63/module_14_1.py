import sqlite3


connection = sqlite3.connect("not_telegram.db", isolation_level='IMMEDIATE')
cursor = connection.cursor()

# 1 создаём таблицу с полями и типами данных в полях
cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
        )
        ''')
connection.commit()

# 2 заполняем таблицу 10 записями по заданию
for i in range(10):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"user{i+1}",
                    f"example{i+1}@gmail.com",
                    f"{(i+1)*10}",
                    f"1000"))
connection.commit()

# 3 обновляем баланс у каждой 2-ой, согласно задания, записи
cursor.execute("SELECT * FROM Users")
users3 = cursor.fetchall()
for user3 in users3:
    rownum = int(user3[0])
    if rownum % 2 != 0:
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", ('500', f'{rownum}'))
    else:
        pass
connection.commit()

# 4 удаляем каждую 3ую запись
cursor.execute("SELECT * FROM Users")
users4 = cursor.fetchall()
counter = 0
trigger = 0
for user4 in users4:
    rownum = int(user4[0])
    if counter == 0 or trigger == 3:
        cursor.execute("DELETE FROM Users WHERE id = ?", (f'{rownum}',))
        counter = 0
        trigger = 0
    else:
        pass
    trigger += 1
    counter += 1
connection.commit()

# 5 отсеаем пассажира которому 60 лет остальных выводим в консоль
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users5 = cursor.fetchall()
for user5 in users5:
    print(f"Имя: {user5[0]} | Почта: {user5[1]} | Возраст: {user5[2]} | Баланс: {user5[3]}")
connection.commit()
connection.close()
