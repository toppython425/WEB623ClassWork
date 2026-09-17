even_numbers = 0
odd_numbers = 0
number = input('Введите число или 0 для остановки программы: ')

while number != '0':
    try:
        number = int(number)
    except ValueError:
        print('Ошибка можно вводить только целые числа!')
    else:
        if number % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
    number = input('Введите число или 0 для остановки программы: ')

print(f'Количество четных: {even_numbers}')
print(f'Количество нечетных: {odd_numbers}')
