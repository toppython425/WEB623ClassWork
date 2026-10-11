# Глобальная область видимости.
a = 4
print(f'Global a: {a}')


def my_func():
    print(f'local a: {a}')


my_func()
print()

# Локальная область видимости.
c = 30
print(f'Global c: {c}')


def my_func1():
    c = 40
    print(f'local с: {c}')


my_func1()
print(f'Global c: {c}')


# Локальная область видимости.

def print_text(text):  # text = user_text
    print(text)


user_text = input('Введите текст для отображения: ')
print_text(user_text)
