day = 13
print('Сегодня пятница, {:10d}'.format(day))
print('Сегодня пятница, {:<10d}'.format(day))
print('Сегодня пятница, {:*<10d}'.format(day))
print('Сегодня пятница, {:*>10d}'.format(day))
print('Сегодня пятница, {:*^10d}'.format(day))

day = 13
month = 10
hour = 15
print('Сегодня пятница: {1:10d}.{0:d} - {2:d} часов'.format(month, day, hour))
#                                                              0    1     2

day = 'пятница'
month = 'сентябрь'
daytime = 'утро'
print('Сегодня пятница: {1:*>10}.{0}.{2:*<10}'.format(month, day, daytime))
print('Сегодня пятница: {day:*>10}.{month}.{daytime:*<10}'.format(month=month, day=day, daytime=daytime))


day_time = 13
pi_num = 3.14159265
print('Сегодня пятница: {0:*>10.2f}'.format(day_time))
print('Число pi: {0:*>10.4f}'.format(pi_num))

