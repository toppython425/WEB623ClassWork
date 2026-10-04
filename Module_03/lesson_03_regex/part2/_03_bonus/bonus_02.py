import re

my_str = """2024 Календарь соревнований:
07.04.2024 - Гран При Японии;
21.04.2024 - Гран При Китая."""

patt = '-;:. '
pattern = re.compile(fr'[{patt}]')
new_str = re.sub(pattern, '**', my_str)
print(new_str)

my_str = """2024 Календарь соревнований:
07.04.2024 - Гран При Японии,
07.04.2024 - Гран При Японии.
21.04.2024 - Гран При Китая;
05.05.2024 - Гран При Майами."""

pattern = re.compile(r'[-,;:\n ]+')
my_str_split = re.split(pattern, my_str)
print(my_str_split)

new_str_split = []
for word in my_str_split:
    if word.endswith('.'):
        word = word[:-1]
    new_str_split.append(word)
print(new_str_split)


import re

text = "Python - это язык программирования. Регулярные выражения - мощный инструмент."

pattern = re.compile(r'[А-ЯЁA-Z]\w*')
word = re.findall(pattern, text)
print(word)