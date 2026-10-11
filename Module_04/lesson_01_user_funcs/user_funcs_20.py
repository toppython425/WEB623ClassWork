def display_planet_address(*args, **kwargs):
    if args:
        for item in args:
            print(item)

    if kwargs:
        for key, value in kwargs.items():
            print(f'{key}: {value}')


if __name__ == '__main__':
    display_planet_address('Дмитрий', 37, planet='Земля', star='Солнце')
    print()
    display_planet_address('Дмитрий', 37)
    print()
    display_planet_address(planet='Земля', star='Солнце')

