import string as stringmod


def remove_from_string(string: str, *args):
    for symbol in args[0]:
        string = string.replace(symbol, '')
    return string


if __name__ == '__main__':
    print(remove_from_string('О! Смотри, можно удалить - все знаки препинания сразу!', stringmod.punctuation))
