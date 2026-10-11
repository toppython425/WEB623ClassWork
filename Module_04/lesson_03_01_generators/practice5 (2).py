# def repeat_message(message, times):
#     for i in range(times):
#         yield message

# if __name__ == '__main__':
#     try:
#         user_msg = input('Введите сообщение: ')
#         repeat_count = int(input('Введиите количество повторений: '))

#         if repeat_count < 0:
#             print('Ошибка: количество повторений не может быть отрицательным')
#         else:
#             print('Результат: ')
#             for msg in repeat_message(user_msg, repeat_count):
#                 print(msg)
#     except ValueError:
#         print('Ошибка, количество повторений должно быть целым числом')

# def range_with_step(start, end, step):
#     current = start
#     if step > 0:
#         while current < end:
#             yield current
#             current += step
#     elif step < 0:
#         while current > end:
#             yield current
#             current += step

# if __name__ == '__main__':
#     try:
#         start_value = int(input('Введите начало диапазона: '))
#         end_value = int(input('Введите конец диапазона: '))
#         step_value = int(input('Введите шаг: '))

#         if step_value == 0:
#             print('Ошибка: шаг не может быть равен нулю.')
#         else:
#             print('Результат:')
#             collected = list(range_with_step(start_value, end_value, step_value))
#             if collected:
#                 for num in collected:
#                     print(num)
#             else:
#                 print('Диапазон пуст')
#     except ValueError:
#         print('Ошибка, можно вводить только целые числа')

def filter_and_square(numbers, threshold):
    for num in numbers:
        if num > threshold:
            yield num ** 2

if __name__ == '__main__':
    try:
        user_input = input('Введите список чисел через пробел: ')
        numbers_list = list(map(int, user_input.split()))

        threshold_value = int(input('Введите порог: '))

        squares = list(filter_and_square(numbers_list, threshold_value))
        if squares:
            for square in squares:
                print(square)
        else:
            print('Нет чисел, удовлетворяющих условию')
    except ValueError:
        print('Ошибка, можно вводить только целые числа')
