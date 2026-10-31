# animals_dict = {'cat': 'котейка', 'dog': 'собачка'}
# new_animals = {'dog': 'собака', 'owl': 'сова', 'parrot': 'попугай'}
# animals_dict.update(new_animals)
# print(animals_dict)

# animals_dict = {'cat': 'кот', 'dog': 'собака'}
# # print(animals_dict['bird'])
#
# word = 'bird'
# if word in animals_dict:
#     print(animals_dict[word])
# else:
#     print(f'Значение ключа {word} нет в словаре.')
#
# try:
#     print(animals_dict[word])
# except KeyError:
#     print(f'Значение ключа {word} нет в словаре.')


animals_dict = {'cat': 'кот', 'dog': 'собака'}
get_animal_01 = animals_dict.get('cat')
print(get_animal_01)
get_animal_02 = animals_dict.get('bird')
print(get_animal_02)
get_animal_03 = animals_dict.get('bird', 'Не знаю таких слов')
print(get_animal_03)
print(animals_dict)

animal_default_01 = animals_dict.setdefault('dog')
print(animal_default_01)
print(animals_dict)

animal_default_02 = animals_dict.setdefault('bird')
print(animal_default_02)
print(animals_dict)

animal_default_03 = animals_dict.setdefault('snake', 'змея')
print(animal_default_03)
print(animals_dict)

animal_default_04 = animals_dict.setdefault('dog', 'собачка')
print(animal_default_04)
print(animals_dict)
