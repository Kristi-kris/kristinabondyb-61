parts = input("Целые числа через пробел: ").split()
numbers = [int(p) for p in parts]

new_numbers = [abs(n) if n < 0 else n for n in numbers]

print(f"Исходный: {numbers}")
print(f"Новый: {new_numbers}")