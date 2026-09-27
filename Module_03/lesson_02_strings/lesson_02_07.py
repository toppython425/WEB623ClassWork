# string_alnum = '123abc'
# print(string_alnum.isalnum())
# string_alnum = '123abc*'
# print(string_alnum.isalnum())
#
# user_password = input('Введите желаемый пароль: ')
# if user_password.isalnum():
#     if 8 <= len(user_password) <= 12:
#         if user_password not in ['qwerty12345', '12345qwerty']:
#             print('Ваш пароль сохранен')
#         else:
#             print('Ваш пароль ненадежен')
#     else:
#         print(f'Длина пароля должна быть от 8 до 12 символов включительно!')
# else:
#     print('Допустимы только буквы и цифры!')
from itertools import count

string_alpha = 'abcdefабвгд'
print(string_alpha.isalpha())
string_alpha = 'abcdefабвгд12345'
print(string_alpha.isalpha())

string_digit = '1234567890'
print(string_digit.isdigit())

if string_digit.isdigit():
    print(int(string_digit))
print()

number = '12.55'
if number.count('.') == 1:
    if number.replace('.', '').isdigit():
        print(float(number))
print()

string_space = '  \n\t\r  '
print(string_space.isspace())
print()

string_lower = 'hello1234*!#'
print(string_lower.islower())
string_lower ='hEllo1234*!#'
print(string_lower.islower())
print()

string_upper = 'HELLO1234*!#'
print(string_upper.isupper())
string_upper ='HEllO1234*!#'
print(string_upper.isupper())
print()

string_title = "Hello World"
print(string_title.istitle())
string_title = "Hello world"
print(string_title.istitle())
