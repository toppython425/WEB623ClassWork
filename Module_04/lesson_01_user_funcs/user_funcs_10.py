def calc_result_sum(numbers: str):
    numbers_list = prepare_numbers(numbers)
    result_sum = 0
    for number in numbers_list:
        result_sum += int(number)
    return result_sum


def calc_result_product(numbers: str):
    numbers_list = prepare_numbers(numbers)
    result_sum = 1
    for number in numbers_list:
        result_sum *= int(number)
    return result_sum


def prepare_numbers(numbers: str):
    numbers_list = numbers.split()
    return numbers_list


def main():
    user_numbers = input('Введите числа через пробел: ')
    user_choice = input('1 - сумма, 2 - произведение: ')
    if user_choice == '1':
        print(f'Ваша сумма: {calc_result_sum(user_numbers)}')
    elif user_choice == '2':
        print(f'Ваше произведение: {calc_result_product(user_numbers)}')
    else:
        print(f'Ошибка ввода! Повторно запустите программу.')


if __name__ == '__main__':
    main()
