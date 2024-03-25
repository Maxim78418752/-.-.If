import calendar
year = int(input('Введите год: '))

if calendar.isleap(year):
    print('Год високосный.')
else:
    print('Год не високосный.')