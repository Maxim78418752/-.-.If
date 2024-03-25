package_weight = float(input("Введите вес посылки в кг: "))
if package_weight <= 2:
    print('стоимость доставки 50 руб.')

elif package_weight > 2 and package_weight <= 10:
    print('Стоимость доставки ', 50 + (package_weight - 2) * 20, 'руб.')

else:
    print('Стоимость доставки 200 руб.')