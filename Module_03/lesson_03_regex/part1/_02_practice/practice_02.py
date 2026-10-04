"""
Задание 2. Поиск правильных IP-адресов

Ситуация: системный администратор передал нам большой набор данных, состоящий из чисел.
Среди этих чисел встречаются IPv4-адреса.

Задача — написать программу, которая находит все корректные IPv4-адреса в тексте и выводит их в консоль.
IPv4-адрес состоит из четырёх чисел, разделённых точками, где каждое число находится в диапазоне
от 0 до 255.
192.168.111.111
"""

import re


# # Определение текста для анализа
# my_text = "Серверы доступны по адресам: 192.168.1.1, 256.256.256.256, 127.0.0.1, 0.0.0.0, 300.300.300.300."
#
# # Создание регулярного выражения для поиска IP-адресов
# pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
#
# # Фильтрация корректных IP-адресов
# ip_addresses = re.findall(pattern, my_text)
# print(ip_addresses)
#
# # Фильтрация корректных IP-адресов
# valid_ips = []
# for ip in ip_addresses:
#     parts = ip.split('.')
#     print(parts)
#     if all(0 <= int(part) <= 255 for part in parts):
#         valid_ips.append(ip)
#
# # Вывод найденных корректных IP-адресов
# print(f'Корректные IP-адреса: {valid_ips}')

def display_correct_ips(text):
    pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    # Фильтрация корректных IP-адресов
    ip_addresses = re.findall(pattern, text)
    print(ip_addresses)

    # Фильтрация корректных IP-адресов
    valid_ips = []
    for ip in ip_addresses:
        parts = ip.split('.')
        # print(parts)
        if all(0 <= int(part) <= 255 for part in parts):
            valid_ips.append(ip)

        # for part in parts:
        #     if 0 <= int(part) <= 255:
        #         continue
        #     else:
        #         break
        # else:
        #     valid_ips.append(ip)

    # Вывод найденных корректных IP-адресов
    print(f'Корректные IP-адреса: {valid_ips}')


if __name__ == '__main__':
    my_text = "Серверы доступны по адресам: 192.168.1.1, 256.256.256.256, 127.0.0.1, 0.0.0.0, 300.300.300.300."
    display_correct_ips(my_text)
