class Animal:

    def __init__(self, name):
        self.name = name

    def breathe(self):
        return f'Животное {self.name} дышит'

    def eat(self, food):
        return f'Животное {self.name} ест {food}'

    def display(self):
        print(f'Имя - {self.name}')


class Fish(Animal):

    def __init__(self, name, specie):
        super().__init__(name)
        self.specie = specie

    # расширение поведения
    def breathe(self):
        base_breathe = super().breathe()
        return f'{base_breathe}\nЭто {self.specie} дышит жабрами'

    def swim(self):
        return f'{self.name}, {self.specie} умеет плавать'

    # переопределение НО должно возвращать тот же тип данных
    def display(self):
        print(f'Это рыба вида {self.specie} ее зовут {self.name}')


class Elefant(Animal):

    def __init__(self, name, specie, gender):
        super().__init__(name)
        self.specie = specie
        self.gender = gender

    # переопределение НО должно возвращать тот же тип данных
    def breathe(self):
        return f'{super().breathe()}\nЭто слон породы {self.specie} дышит легкими'

    def eat(self, food):
        return f'{self.specie}, {self.name} ест {food}'

    def run(self):
        return f'{self.name}, {self.specie}, {self.gender} бегает'

    # расширение поведения
    def display(self):
        super().display()
        print(f'Вид - {self.specie}')
        print(f'Пол - {self.gender}')


if __name__ == '__main__':
    animal = Animal("Жулик")
    print(animal.breathe())
    print(animal.eat('еда'))
    animal.display()
    print()

    fish = Fish('Немо', 'Рыба-клоун')
    print(fish.breathe())
    print(fish.eat('водоросли'))
    print(fish.swim())
    fish.display()
    print()

    elefant = Elefant('Боб', 'Индийский', 'Самец')
    print(elefant.breathe())
    print(elefant.eat('Трава'))
    print(elefant.run())
    elefant.display()
