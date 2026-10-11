import random


def get_random_gift(gifts):
    gift = random.sample(gifts, 1)[0]
    return gift


if __name__ == '__main__':
    gifts1 = ['барбариски', "мячик", "машинка", "конструктор"]
    gifts2 = ['леденцы', 'мишка', 'самолетик', 'вертолётик']
    while True:
        user_choice = input(
            f'Введите:\n1 - для подарков: {', '.join(gifts1)};\n2 - для подарков: {', '.join(gifts2)};\n0 - для остановки.\nВаш выбор: ')
        if user_choice == '0':
            break
        elif user_choice == '1':
            print(f'Ваш подарок: {get_random_gift(gifts1)}')
        elif user_choice == '2':
            print(f'Ваш подарок: {get_random_gift(gifts2)}')
        else:
            print(f'Неверная команда!')
