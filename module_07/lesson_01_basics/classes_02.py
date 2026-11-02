class CakeForm:

    def __init__(self, dough, form, cooking_time=40):
        self.dough = dough
        self.form = form
        self.cooking_time = cooking_time
        print(f'Я кекс из теста: {self.dough}, в форме: {self.form}, время готовки: {self.cooking_time}')



if __name__ == '__main__':
    cake1 = CakeForm('Пшеничное', 'Круглая')
    cake2 = CakeForm('Овсяное', 'Квадратная', 60)
