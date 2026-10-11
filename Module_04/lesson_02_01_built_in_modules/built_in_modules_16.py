from platform import processor
from multiprocessing import Pool
from datetime import datetime


def square(x):
    return x ** 2


if __name__ == '__main__':
    print(processor())
    print(datetime.now())
    user_pc = {
        "AMD64 Family 25 Model 33 Stepping 2, AuthenticAMD": {'cores': 8, 'threads': 16}
    }
    cores = user_pc[processor()]['cores']
    with Pool(processes=cores) as pool:
        numbers = list(range(100000000))
        results = pool.map(square, numbers)

    print(f'Квадраты чисел: {results[-1]}')
    print(datetime.now())
