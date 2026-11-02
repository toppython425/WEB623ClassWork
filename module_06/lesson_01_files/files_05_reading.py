def display_data_from_file(file_path):
    with open(file_path, 'rt', encoding='utf-8') as file:
        for line in file:
            print(line.rstrip())


def get_data_from_file(file_path: str) -> list[str]:
    content = []
    with open(file_path, 'rt', encoding='utf-8') as file:
        for line in file:
            content.append(line.rstrip())
    return content


def get_data_from_file_readlines(file_path: str) -> list[str]:
    with open(file_path, 'rt', encoding='utf-8') as file:
        content = file.readlines()
    return content


def read_data_from_file_gen(file_path: str):
    with open(file_path, 'rt', encoding='utf-8') as file:
        for line in file:
            yield line


if __name__ == '__main__':
    my_filepath = r'data_files\file_for_reading.txt'
    # display_data_from_file(my_filepath)
    print(get_data_from_file(my_filepath))
    print(get_data_from_file_readlines(my_filepath))
    data = []
    for line in read_data_from_file_gen(my_filepath):
        input('Нажмите ввод для чтения следующей строки')
        data.append(line)
    print(data)
