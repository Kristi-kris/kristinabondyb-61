first = int(input("Первое целое число: "))
second = int(input("Второе целое число: "))
third = int(input("Третье целое число: "))

if first <= second and first <= third:
    smallest = first
elif second <= first and second <= third:
    smallest = second
else:
    smallest = third

print(f"Минимум: {smallest}")