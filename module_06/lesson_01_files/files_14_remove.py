import os
import shutil

my_path = r'dir_02/file1_new_place.txt'

try:
    os.remove(my_path)
except FileNotFoundError:
    print(f'Файл не найден в указанном расположении:\n{my_path}')
else:
    print('Файл успешно удален')

my_path = r'dir_02'
try:
    shutil.rmtree(my_path)
except FileNotFoundError:
    print(f'Файл/папка не найдены')
else:
    print(f'Файл успешно удален.')
