def calculate_way(v, t):
    way = v * t
    return way


if __name__ == '__main__':
    data_dict1 = {'v': 60, 't': 3}
    data_dict2 = {'t': 3, 'v': 50}
    data_dict3 = {'v': 100, 't': 3}
    distance_data = [
        data_dict1,
        data_dict2,
        data_dict3
    ]
    data_tuple = (50, 3)
    for row, data in enumerate(distance_data):
        print(f'Matrix row {row + 1} distance: {calculate_way(**data)}')
