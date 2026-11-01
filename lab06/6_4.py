parts = input("Целые числа через пробел: ").split()
numbers = [int(p) for p in parts]

selected = [n for n in numbers if n < 0 and n % 2 != 0]

print(f"Выборка: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Сортированная копия: {sorted(selected)}")