from datetime import datetime

try:
    print('Код который может вызвать ошибку: ')
    num = int(input('Введите целое число: '))
    print(10 / num)
    # raise KeyError
except ValueError:
    print('Введено неверное значение, допустимы только целые числа.')
except ZeroDivisionError:
    print('Попытка деления на 0')
except Exception as ex:
    print('Код на случай неожиданного исключения')
    print(type(ex).__name__)
    with open('logging.log', 'a', encoding='utf-8') as file:
        file.write(f'{datetime.now().strftime('%d-%m-%Y - %H:%M:%S')} >>> {type(ex).__name__}\n')
else:
    print('Код который будет выполнен ТОЛЬКО если исключений НЕ ВОЗНИКЛО.')
    print(num * 2)
finally:
    print('Код который выполнится в любом случае.')
    print('Программа завершила работу')





