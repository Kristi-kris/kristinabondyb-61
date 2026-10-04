rejected_attempts = 0
number = int(input("Введите положительное целое число: "))

while number <= 0:
    rejected_attempts += 1
    number = int(input("Число должно быть положительным. Повторите ввод: "))

print(f"Квадрат: {number ** 2}")
print(f"Отклонённых попыток: {rejected_attempts}")