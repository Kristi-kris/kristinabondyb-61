parts = input("Целые числа через пробел: ").split()

if not parts:
    print("Нет данных")
else:
    numbers = [int(p) for p in parts]
    count = len(numbers)
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / count
    print(f"Количество {count}, сумма {total}, минимум {minimum}, максимум {maximum}, среднее {average:.2f}")