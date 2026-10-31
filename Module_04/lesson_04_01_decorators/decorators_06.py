from datetime import datetime
from functools import wraps
import time


def log_stream(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{datetime.now()} >> Вызов функции {func.__name__} с аргументами {args} и {kwargs}')
        return func(*args, **kwargs)

    return wrapper


def log_to_file(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(r'logs\log_file.log', 'a', encoding='utf-8') as file:
            file.write(f'{datetime.now()} >> Вызов функции {func.__name__} с аргументами {args} и {kwargs}\n')
        return func(*args, **kwargs)

    return wrapper


@log_stream
@log_to_file
def display_my_address(*args, **kwargs):
    if args:
        for item in args:
            print(item)
    if kwargs:
        for key, value in kwargs.items():
            print(f'{key}: {value}')


@log_stream
@log_to_file
def get_my_space_address(*args, **kwargs):
    return args, kwargs


if __name__ == '__main__':
    display_my_address('Дмитрий', 37, planet='Земля', star='Солнце')
    time.sleep(2)
    display_my_address('Илон', 55, planet='Марс', star='Солнце')
    print(display_my_address.__name__)

    space_data = get_my_space_address('Дмитрий', 37, planet='Земля', star='Солнце')
    print(space_data)
