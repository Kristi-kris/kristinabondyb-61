count = int(input("Количество чисел (не меньше 1): "))
if count < 1:
    raise ValueError("Количество чисел должно быть не меньше 1")

first_number = int(input("Число 1: "))
total = first_number
positive_count = 0
if first_number > 0:
    positive_count += 1
maximum = first_number

for index in range(1, count):
    number = int(input(f"Число {index + 1}: "))
    total += number
    if number > 0:
        positive_count += 1
    if number > maximum:
        maximum = number

print(f"Сумма: {total}")
print(f"Положительных чисел: {positive_count}")
print(f"Максимум: {maximum}")