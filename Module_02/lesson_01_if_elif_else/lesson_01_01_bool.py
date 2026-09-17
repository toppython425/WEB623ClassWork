print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))
print(bool(0))
print(bool(0.0))
print(bool(None))
print()

print(bool("Some string"))
print(bool(['item1', 'item2']))
print(bool(('item1', 'item2')))
print(bool({'key1': 'value1'}))
print(bool({'item1', 'item2'}))
print(bool(2))
print(bool(0.001))
print()

data = [
    {'key': 'value'}
]

if data:
    print(f'Обработка данных: {data}')
else:
    print('Данные не получены.')

if not data:
    print('Данные не получены.')
else:
    print(f'Обработка данных: {data}')
