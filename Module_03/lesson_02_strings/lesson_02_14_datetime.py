from datetime import datetime, timedelta

# получение текущей даты и времени
now = datetime.now()
print(now)

# задать свою дату и время
date1 = datetime(2025, 7, 27, 15, 20, 30)
date2 = datetime(year=2025, month=7, day=27, hour=15, minute=20, second=30)
print(date1)
print(date2)

# задать временной промежуток
delta = timedelta(days=5, hours=12, minutes=30, seconds=45)
print(delta)

# сегодня
today = datetime.today()
print(today)

# вычисление будущей даты
future_date = today + delta
print(future_date)

# вычисление разницы между датами
date1 = datetime(2025, 1, 1)
date2 = datetime(2026, 9, 19)
delta = date2 - date1
print(delta)

# получение объекта даты из строк разного вида
str_date1 = '10.05.2025'
str_date2 = '26-June-2025'
str_date3 = '5 Jan, 11'

first_date = datetime.strptime(str_date1, '%d.%m.%Y')
print(first_date, type(first_date))
second_date = datetime.strptime(str_date2, '%d-%B-%Y')
print(second_date, type(second_date))
third_date = datetime.strptime(str_date3, '%d %b, %y')
print(third_date, type(third_date))

# форматирование даты и времени
formatted_date = datetime.strptime(str_date1, '%d.%m.%Y').strftime('%d-%B-%Y')
print(formatted_date, type(formatted_date))