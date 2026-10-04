order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")
first_item = input("Первая позиция (мячи): ")
first_quantity = int(input("Количество: "))
first_price = float(input("Цена единицы, руб.: "))
second_item = input("Вторая позиция (скакалки): ")
second_quantity = int(input("Количество: "))
second_price = float(input("Цена единицы, руб.: "))
delivery = float(input("Доставка, руб.: "))
paid = float(input("Внесённая сумма, руб.: "))

first_cost = first_quantity * first_price
second_cost = second_quantity * second_price
goods_total = first_cost + second_cost
grand_total = goods_total + delivery
total_quantity = first_quantity + second_quantity
change = paid - grand_total

print(f"\nЗаказ: {order_name}")
print(f"Заказчик: {customer_name}")
print(f"{first_item} | {first_quantity} | {first_price:.2f} | {first_cost:.2f}")
print(f"{second_item} | {second_quantity} | {second_price:.2f} | {second_cost:.2f}")
print(f"Товары без доставки: {goods_total:.2f} руб.")
print(f"Итого с доставкой: {grand_total:.2f} руб.")
print(f"Общее количество единиц: {total_quantity}")
print(f"Сдача: {change:.2f} руб.")
