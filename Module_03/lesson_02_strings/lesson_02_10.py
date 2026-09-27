import os

normal_string = 'Эта строка\n-обычная строка'
print(normal_string)

raw_string = r'Эта строка\n-сырая строка'
print(raw_string)

# err_raw1 = r'\'
# noerr_raw2 = r'\\abc\\\\\\\abc\\'
# print(noerr_raw2)

print(os.path.exists(r'.\lesson_02_05.py'))

user_name = input('Введите ваше имя: ')
print(fr'.\filename_{user_name}.txt')
