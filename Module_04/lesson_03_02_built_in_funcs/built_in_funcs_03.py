my_list = [x for x in range(1, 6)]
map_func = map(lambda x: 2 ** x, my_list)
print(map_func)
degrees_list_from_map = list(map_func)
print(degrees_list_from_map)

for x in map(lambda x: 2 ** x, my_list):
    print(x, end=' ')
print()

# my_list.append('Привет')

def square_2(x):
    if type(x) is int:
        return 2 ** x
    else:
        return 'Данные неподходящего типа'


for x in map(square_2, my_list):
    print(x, end=' ')
