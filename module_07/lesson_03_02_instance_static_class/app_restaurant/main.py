from Classes.ClassOrders import RestaurantOrder

if __name__ == '__main__':
    # Основная программа
    order1 = RestaurantOrder(1, "Салат Цезарь")
    order2 = RestaurantOrder(2, ["Пицца Маргарита", "Кофе"])
    order3 = RestaurantOrder(1, "Чай")

    # Проверяем доступность столов
    print(f'Стол 3 свободен? {"Да" if RestaurantOrder.is_table_available(3) else "нет"}')  # True
    print(f'Стол 1 свободен? {"Да" if RestaurantOrder.is_table_available(1) else "нет"}')  # True

    # Вывод общего количества заказов
    print(RestaurantOrder.get_total_orders_info())

    # Показываем заказы по столам
    RestaurantOrder.show_orders()
    print(RestaurantOrder.tables)
