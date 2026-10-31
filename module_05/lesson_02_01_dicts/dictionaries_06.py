def calculate_price(fruits_dict, fruit, weight):
    price = fruits_dict[fruit] * weight / 1000
    return price


if __name__ == '__main__':
    user_fruit = input('Выберете фрукт: ')
    fruits = {
        'яблоки': 400,
        'груши': 200,
        'персики': 600
    }
    if user_fruit not in fruits:
        print(f'{user_fruit} нет в ассортименте')
    else:
        fruit_weight = float(input('Введите вес в граммах: '))
        result = calculate_price(fruits, user_fruit, fruit_weight)
        print(f'Стоимость: {result} рублей')
