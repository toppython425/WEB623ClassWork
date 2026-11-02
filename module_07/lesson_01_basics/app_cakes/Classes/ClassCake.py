class CakeForm:

    def __init__(self, dough, form, *args, cooking_time=40):
        self.dough = dough
        self.form = form
        self.cooking_time = cooking_time
        if not args:
            self.ingredient_list = []
        else:
            self.ingredient_list = list(args)
        self.recipe = {
            'dough': None,
            'form': None,
            'ingredient_list': [],
            'cooking_time': self.cooking_time
        }

    def make_dough(self):
        print(f'Мы замешиваем тесто: {self.dough}')
        self.recipe['dough'] = self.dough

    def make_form(self):
        print(f'Мы выкладываем тесто в форму {self.form}')
        self.recipe['form'] = self.form

    def add_ingredient(self, ingredient):
        self.ingredient_list.append(ingredient)
        print(f'Добавлен {ingredient}')
        self.recipe['ingredient_list'] = self.ingredient_list

    def add_ingredients(self, *args):
        self.ingredient_list.extend(args)
        print(f'Добавлены {', '.join(args)}')
        self.recipe['ingredient_list'] = self.ingredient_list

    def cook_cake(self, user_time=40):
        if user_time > self.cooking_time:
            print(f'За {user_time} минут кекс {self.recipe} сгорит!')
            return None
        else:
            self.recipe['cooking_time'] = user_time
            print(f'Мы готовим {user_time} минут кекс {self.recipe}.')
            return self.recipe


if __name__ == '__main__':
    cake1 = CakeForm('Пшеничное', 'Круглая')
    cake2 = CakeForm('Овсяное', 'Квадратная', 60)
    cake1.make_dough()
    cake1.make_form()
    print(cake1.recipe)
    print(cake2.recipe)
