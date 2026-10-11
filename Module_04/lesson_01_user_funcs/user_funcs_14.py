# print(sum([1, 2, 3], 4))


def new_sum(*args, start_value=0):  # интерфейс-зависимая
    """
    :param args:
        числа для суммирования
    :param start_value:
        базовое значение
    :return:
        сумма переданных чисел
    """
    # print(args)
    # print(type(args))
    args_list = list(args)
    total_value = start_value
    for num in args_list:
        total_value += num
    return total_value


def new_sum_safe(*args, start_value=0):  # интерфейс-независимая
    """
    :param args:
        числа для суммирования
    :param start_value:
        базовое значение
    :return:
        сумма переданных чисел
    """
    args_list = list(args)
    total_value = start_value
    for num in args_list:
        if type(num) is int or type(num) is float:
            total_value += num
        else:
            print(f'В данных есть объекты которые на являются числом: {num}')
    return total_value


if __name__ == '__main__':
    print(new_sum(1, 2, 3, 4, 5, start_value=10))
    print(new_sum_safe(1, 2, 3, 'a', 4, 5, start_value=10))
