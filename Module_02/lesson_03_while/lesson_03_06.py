shopping_list = []

while True:
    user_input = input('Введите вашу покупку или стоп: ').strip().lower()
    user_sum = 0
    if user_input == 'стоп':
        break
    while True:
        try:
            user_sum = float(input(f'Введите сумму покупки {user_input}: '))
            break
        except ValueError:
            print('Ошибка ввода суммы! Введите число!')
    shopping_list.append([user_input, user_sum])

# print(shopping_list)
print()
"""
[
['кофе', 150.0], 
['булочка', 100.0], 
['печенье', 250.0]
]
"""

if shopping_list:
    while True:
        user_choice = input(
            'Вывести только покупки - 1\nВывести только суммы - 2\nВывести все + итог - 3\nВыход - 0\nВаш выбор: ')
        if user_choice == '0':
            print('Программа завершена: ')
            break
        elif user_choice == '1':
            print('Список покупок:')
            for purchase, price in shopping_list:
                print(purchase)
        elif user_choice == '2':
            print('Список сумм:')
            for purchase, price in shopping_list:
                print(price)
        elif user_choice == '3':
            total_price = 0
            print('Покупки и цены:')
            for purchase, price in shopping_list:
                print(f'Покупка: {purchase}. Цена: {price}.')
                total_price += price
            print(f'Итого покупок: {len(shopping_list)} на сумму: {total_price}')
        else:
            print('Ошибка ввода!')
        print()
else:
    print('Вы ничего не покупали.')
