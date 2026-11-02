class Car:
    wheels = 4

    def __init__(self, brand, color, doors):
        self.brand = brand
        self.color = color
        self.doors = doors

    def drive(self):
        print(f'Автомобиль {self.brand}. Цвет {self.color}. Двери {self.doors} едет! Колеса {self.wheels}')

    @classmethod
    def describe(cls):  # что для работы с @classmethod вместо self используем cls везде в теле данного метода
        print(f'Легковые автомобили имеют {cls.wheels} колеса')

    @classmethod
    def change_wheels_quantity(cls, wheels_num):
        Car.check_int_data_type(wheels_num)
        cls.wheels = wheels_num

    @staticmethod
    def check_int_data_type(data):
        if isinstance(data, int):
            return True
        raise TypeError('Неверный тип данных!')

    @staticmethod
    # Если не используются атрибуты (класса или экземпляра) используем >> @staticmethod
    # Вызов через self или объект не вызывает ошибку, но это плохой код поэтому вызываем его через класс
    def general_info():
        print('Автомобили это транспортные средства')


if __name__ == '__main__':
    car_obj = Car('Toyota', 'red', 4)
    car_obj.drive()
    Car.describe()
    print()

    Car.change_wheels_quantity(6)
    Car.describe()
    car_obj.drive()
    print()

    Car.general_info()
    print(car_obj.__dict__)

    car_obj.wheels = 4
    # присваиваем новый (неожиданный) атрибут к конкретному объекту
    # (и теперь он отличается от остальных, что может далее вызвать проблемы)
    # не делайте так! Это не меняет значение атрибута класса,
    # если нужно изменить атрибут класса меняйте его через класс (или @classmethod) если он предусмотрен.
    print(car_obj.__dict__)

    car2 = Car('Honda', 'синий', 4)
    print(car2.__dict__)
    # Car.change_wheels_quantity(6.5)
