import re

text = 'Контактный номер: 81234567890, 71234567890'
pattern = re.compile(r'8\d{10}')
matches = re.findall(pattern, text)
print(matches)

text = 'Контактные номера: +7 (123) 456-78-90, 81234567890, 8-123-456-78-90, 8------()-----'
pattern = re.compile(r'\+?\d[\d\s\-()]{10,16}')
matches = re.findall(pattern, text)
print(matches)

user_phone = input('Введите номер телефона в формате:\n+***(**)******* для РБ\n+*(***)******* для РФ:\n')
pattern1 = re.compile(r'\+\d{3}\(\d{2}\)\d{7}')
pattern2 = re.compile(r'\+\d{1}\(\d{3}\)\d{7}')
value1 = bool(re.match(pattern1, user_phone))
value2 = bool(re.match(pattern2, user_phone))
print(value1 or value2)
