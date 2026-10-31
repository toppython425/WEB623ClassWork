animals_set = {"Cat", 'Turtle', 'Snake', 'Dog', "Cat", 'Turtle'}
print(len(animals_set))
print(animals_set)

animals = ["Cat", 'Turtle', 'Snake', 'Dog', "Cat", 'Turtle']
unique_animals = set(animals)
print(unique_animals)
print(list(unique_animals))

set_from_str = set('turtle')
print(set_from_str)

# множество неизменяемое
my_frozenset = frozenset(animals)
print(my_frozenset)

# пустое множество
my_set = set()
print(my_set)

# пустое множество неизменяемое
my_frozenset = frozenset()
print(my_frozenset)
