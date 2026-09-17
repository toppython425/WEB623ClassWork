try:
    raise Exception
except Exception:
    print(f'Хмм... Что то пошло не так')
except ValueError as err:
    print(f'Получено нужное исключение: {type(err).__name__}')

try:
    raise ValueError
except Exception:
    print(f'Хмм... Что то пошло не так')
except ValueError as err:
    print(f'Получено нужное исключение: {type(err).__name__}')

try:
    raise ValueError
except ValueError as err:
    print(f'Получено нужное исключение: {type(err).__name__}')
except Exception:
    print(f'Хмм... Что то пошло не так')


try:
    raise ValueError
except ValueError as err:
    print(f'Получено нужное исключение: {type(err).__name__}')
except Exception as err:
    print(f'Хмм... Что то пошло не так: {type(err).__name__}')
