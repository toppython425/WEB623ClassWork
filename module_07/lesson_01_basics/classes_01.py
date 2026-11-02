class CakeForm(object):

    def make_dough(self):
        print(f'Мы замешиваем тесто')

    def make_form(self):
        print(f'Мы выкладываем тесто в форму')

    def cook_cake(self, time=40):
        if time > 80:
            print(f'За {time} минут кекс сгорит!')
        else:
            print(f'Мы выпекаем кекс {time} минут!')


if __name__ == '__main__':
    cake1 = CakeForm()
    cake2 = CakeForm()

    print(cake1)
    print(cake2)
    print(cake1 is cake2)

    # cake3 = cake1   # не делайте так!
    # print(cake3 is cake1)
    # print(cake1)
    # print(cake3)

    cake1.make_dough()
    cake1.make_form()
    cake1.cook_cake()
    print()

    cake2.make_dough()
    cake2.make_form()
    cake2.cook_cake(100)