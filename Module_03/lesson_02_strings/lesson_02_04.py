# # my_string1 = 'Hello'
# # my_string2 = 'World'
# # space = ' '
# #
# # new_string = my_string1 + my_string2
# # print(new_string)
# # new_string = my_string1 + space + my_string2
# # print(new_string)
#
#
# my_string1 = 'Hello'
# my_string2 = 'World'
# delimiter = ', '
# new_string = my_string1 + delimiter + my_string2
# print(new_string)
#
# num1 = '1'
# num2 = '1'
# print(num1 + num2)

# my_string = 'Hello'
# mult_string = my_string * 3
# print(mult_string)
# mult_string = ((my_string + ' ') * 3).strip()
# print(mult_string)

my_string = 'Hello World!'
print(len(my_string))
print(type(len(my_string)))

goods = input('Введите наименование товара: ')
if len(goods) <= 10:
    print(f'Товар {goods} добавлен в реестр.')
else:
    print('Ошибка! Наименование товара не может быть больше 10 символов.')

my_string = 'hello WORLD!'
swapped_string = my_string.swapcase()
print(swapped_string)

