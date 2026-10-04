"""
Тип ошибки 2: Некорректное использование метасимволов
Возникает, когда метасимволы, такие как ., *, +, не экранированы в случае использования
их как обычных символов.
Пример ошибки:
"""
import re

text = "Цена: $10A50"
text1 = "Цена: $10,50 $10.50"
pattern = re.compile(r'\$\d+\.\d{2}')
pattern1 = re.compile(r'\$\d+[.,]+\d{2}')
matches1 = re.findall(pattern, text1)
matches2 = re.findall(pattern1, text1)
print(matches1)
print(matches2)
