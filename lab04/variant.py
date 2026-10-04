count = int(input("Количество чисел: "))
if count < 0:
    raise ValueError("Количество чисел не может быть отрицательным")

selected_count = 0
selected_sum = 0

for index in range(count):
    number = int(input(f"Число {index + 1}: "))
    if number >= 0:
        selected_count += 1
        selected_sum += number

print(f"Количество положительных чисел: {selected_count}")
print(f"Сумма положительных чисел: {selected_sum}")
