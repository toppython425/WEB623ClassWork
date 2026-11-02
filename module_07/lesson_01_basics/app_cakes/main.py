from Classes.ClassCake import CakeForm

if __name__ == '__main__':
    # cake1 = CakeForm("Пшеничное", "Круглая", 'Ром', 'Марципан')
    # cake1.make_dough()
    # cake1.make_form()
    # cake1.add_ingredient('Изюм')
    # cake1.add_ingredients('Курага', 'Чернослив')
    # print()
    # print(cake1.cook_cake())
    # print(cake1.cook_cake(100))
    # print()

    cake_2 = CakeForm("Овсяное", "Квадратная", cooking_time=60)
    cake_2.make_dough()
    cake_2.make_form()
    print(cake_2.cook_cake())
    print(cake_2.cook_cake(70))
