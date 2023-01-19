# Программа "Автодилер"

first_price = int(input("Введите стоимость автомобиля (в USD) без наценок: "))
tax = first_price / 100 * 15
reg_fee = first_price / 100 * 10
agency_fee = 200
shipping_cost = 100
print("Окончательная цена автомобиля составляет: ", first_price + tax + reg_fee + agency_fee + shipping_cost, "$")
