parts = input("Целые числа через пробел: ").split()

if not parts:
    print("Нет данных")
else:
    numbers = [int(p) for p in parts]
    maximum = max(numbers)
    positions = [i for i, n in enumerate(numbers) if n == maximum]
    print(positions)