numbers_count = 0
even_numbers = 0
odd_numbers = 0

while numbers_count != 6:
    number = int(input('Введите число или 0 для остановки программы: '))
    if number == 0:
        break
    elif number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
    numbers_count += 1
else:
    print(f'Вы ввели все 6 чисел!')

print(f'Количество четных: {even_numbers}')
print(f'Количество нечетных: {odd_numbers}')
