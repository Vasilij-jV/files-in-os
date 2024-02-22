# -*- config: utf8 -*-

import time
import os


directory = os.path.normpath('C:/windows/help')

# Обход каталога
for dirpath, dirnames, filenames in os.walk(directory):
    print(dirpath, dirnames, filenames)


# Формирование полного пути к файлам
for dirpath, dirnames, filenames in os.walk(directory):
    print(dirpath, dirnames, filenames)
    for file in filenames:
        full_path_file = os.path.join(dirpath, file)
        print(full_path_file)


# Получение и отображение времени последнего изменения файла
for dirpath, dirnames, filenames in os.walk(directory):
    print(dirpath, dirnames, filenames)
    for file in filenames:
        full_path_file = os.path.join(dirpath, file)
        secs = os.path.getmtime(full_path_file)
        file_time = time.gmtime(secs)
        if file_time[0] == 2020 and file_time[1] == 5:
            print(full_path_file, secs)


# Получение размера файла
for dirpath, dirnames, filenames in os.walk(directory):
    print(dirpath, dirnames, filenames)
    for file in filenames:
        full_path_file = os.path.join(dirpath, file)
        size_file = os.path.getsize(full_path_file)
        print(full_path_file, size_file)


# Получение родительской директории файла
for dirpath, dirnames, filenames in os.walk(directory):
    print(dirpath, dirnames, filenames)
    for file in filenames:
        print('-' * 30)
        full_path_file = os.path.join(dirpath, file)
        parent_file = os.path.dirname(full_path_file)
        print(full_path_file, '\n', parent_file)
