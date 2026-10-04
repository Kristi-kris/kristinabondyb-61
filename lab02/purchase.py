price = int(input("Цена одной тетради, руб.: "))
count = int(input("Количество тетрадей: "))
paid = int(input("Переданная сумма, руб.: "))

if price < 0 or count < 0:
	raise ValueError("Цена и количество не могут быть отрицательными")

cost = price * count
if paid < cost:
	raise ValueError("Внесённой суммы недостаточно для оплаты")

change = paid - cost

print(f"Стоимость: {cost} руб.")
print(f"Сдача: {change} руб.")