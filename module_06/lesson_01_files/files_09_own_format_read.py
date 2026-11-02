def get_data_dict_from_file(filename, divider):
    managers_data_dict = {}
    with open(filename, encoding='utf-8') as managers_data:
        for manager_data in managers_data:
            clean_data = manager_data.strip().split(divider)
            # print(clean_data)
            # manager = clean_data[0]
            # company = clean_data[1]
            # head_company = clean_data[2]
            manager, company, head_company = clean_data
            managers_data_dict[(company, head_company)] = manager
    return managers_data_dict


if __name__ == '__main__':
    managers_filename = r'data_files\managers_data_own_format.txt'
    d_managers_data = get_data_dict_from_file(managers_filename, ':')
    for (d_company, d_head_company), d_manager in d_managers_data.items():
        print(f'{d_manager} работает в компании {d_company} которая принадлежит {d_head_company}')
