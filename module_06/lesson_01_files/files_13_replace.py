import os

base_path = 'dir_02/file2.txt'
new_path = 'dir_03/file2.txt'

try:
    os.replace(base_path, new_path)
except FileNotFoundError:
    print(f'Файл не найден!')
except FileExistsError:
    print(f'Такой файл уже существует!')
else:
    print(f'Файл успешно перемещен и/или переименован:\n{os.path.abspath(new_path)}')
print()
