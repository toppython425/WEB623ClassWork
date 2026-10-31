my_dict1 = {}
print(type(my_dict1))
print(my_dict1)

my_dict2 = dict()
print(my_dict2)

employees_dict = {'Петр': 201, 'Мария': 201}
print(employees_dict)
some_dict = {'Петр': 'Имя', 'Python': 'Язык Программирования'}
print(some_dict)
dict_keys_num = {1: 'Очень плохо', 2: 'Плохо', 3: 'Удовлетворительно'}
print(dict_keys_num)
dict_keys_tuple = {('мтс', 'мтс'): 50}
print(dict_keys_tuple)
print()

keyword_dict = dict(name='Петр', python='Язык программирования')
print(keyword_dict)
animals_dict = dict([('cat', 'кот'), ('dog', 'собака'), ('snake', 'змея')])
print(animals_dict)

explanations = {True: 'Ответ верный', False: 'Ответ неверный!'}
user_num = int(input('Введите число меньше 10: '))

if user_num < 10:
    print('Ответ верный')
else:
    print('Ответ неверный!')

print(explanations[user_num < 10])
