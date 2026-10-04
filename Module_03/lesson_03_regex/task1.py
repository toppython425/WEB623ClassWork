import re
text = "Python – это язык программирования. Регулярные выражения – мощный инструмент."
result = re.findall(r'[A-ZА-Я][a-zа-я]*', text)
print(result)