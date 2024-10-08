import os
import time

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = os.path.join(os.getcwd(), file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'\nОбнаружен файл: {file},\n Путь: {filepath},\n Размер: {filesize} байт,\n Время изменения: {formatted_time},\n Родительская директория: {parent_dir}')
        

