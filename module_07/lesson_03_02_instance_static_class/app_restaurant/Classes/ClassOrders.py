"""
Задача 2: Управление заказами ресторана

Ситуация: мы создаем систему управления заказами в ресторане.
Каждый заказ связан с определённым номером стола.
В ресторане есть ограниченное количество столов, и если стол занят, то новый заказ для него не принимается.

Задача: создайте программу, которая позволяет:

Добавлять заказы на определённый стол.
Проверять, свободен ли стол.
Узнавать общее количество заказов.
Отображать все заказы для каждого стола.
"""


class RestaurantOrder:
    total_orders = 0
    tables = {}

    def __init__(self, table_number, order_details):
        self.table_number = table_number
        self.order_details = order_details
        RestaurantOrder.total_orders += 1
        # setdefault устанавливает ключом номер столика и задает значение по умолчанию [],
        # при этом сразу возвращая [] к которому мы тут же .append(order_details)
        if isinstance(order_details, list):
            RestaurantOrder.tables.setdefault(table_number, []).extend(order_details)
        else:
            RestaurantOrder.tables.setdefault(table_number, []).append(order_details)

    @staticmethod
    def is_table_available(table_number):
        return len(RestaurantOrder.tables.get(table_number, [])) == 0

    @classmethod
    def get_total_orders_info(cls):
        return f'Всего заказов: {cls.total_orders}'

    @classmethod
    def show_orders(cls):
        for table, orders in cls.tables.items():
            print(f'Стол №{table}: {', '.join(orders)}')
