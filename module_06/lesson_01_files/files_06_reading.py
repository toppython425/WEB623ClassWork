from os import path

def guests_manager(file_path):
    guest_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        guest_list = file.readlines()
    return len(guest_list), guest_list


if __name__ == '__main__':
    guests_data = r'data_files\guests.txt'
    try:
        guests_count, guests = guests_manager(guests_data)
    except FileNotFoundError:
        print(f'Список гостей не найде в указанном месторасположении >> {guests_data}')
        print(f'Список гостей не найде в указанном месторасположении >> {path.abspath(guests_data)}')
    else:
        print(f'Всего гостей: {guests_count}')
        print(f'Список гостей:\n{''.join(guests)}')
