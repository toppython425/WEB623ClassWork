# # Блоки выполнения для:
# # Условных конструкций
# data = [
#     {'key': 'value'}
# ]
#
# if data:
#     print(f'Обработка данных: {data}')
# else:
#     print('Данные не получены.')
# print()
#
# # циклов:
# counter = 0
# while counter < 5:
#     print('Внутри цикла')
#     counter += 1
# print('Вышли из цикла')
# print()
#
# for i in range(5):
#     print(f'Внутри цикла: i = {i}')
# print('Вышли из цикла')
# print()

# исключения
try:
    print('Провокация')
    # raise Exception
except Exception:
    print("Обход исключения если оно возникло")
else:
    print(f'Код который выполняется если исключения не возникло')
finally:
    print(f'Код который выполняется в любом случае')
print()


# функции
def some_func():
    print('Внутри функции')


some_func()
print()

# классы
class ExampleClass:
    def __init__(self, attr):
        self.attr = attr

    def display_attr(self):
        print(self.attr)


my_obj = ExampleClass('Some Attr')
my_obj.display_attr()
