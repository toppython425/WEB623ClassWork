shopping_list = []

while True:
    # item = input()  # Тут неплохо было бы написать, что программа от меня хочет
    item = input("Введите покупку или стоп для завершения работы программы: ")  # например вот так.
    if item == "стоп":
        break
    shopping_list.append(item)

[print(element) for element in shopping_list]

total_sum = 0

while True:
    user_input = input()  # то же самое замечание, что и выше, что от меня хотят? Как продолжить?
    if user_input.lower() in ['стоп', 'stop']:
        break

    total_sum += int(user_input)

print(total_sum)
