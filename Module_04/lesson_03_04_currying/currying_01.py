def simple_greet(greeting, name):
    print(f'{greeting}, {name}')


def greet_curried(greeting):
    def greet(name):
        print(greeting, name)

    return greet


if __name__ == '__main__':
    simple_greet('Привет', 'Дмитрий')
    base_param = 'Привет,'
    greet_hello = greet_curried(base_param)
    user_name1 = input('Введите имя пользователя: ')
    greet_hello(user_name1)
    greet_hello('Петр')
