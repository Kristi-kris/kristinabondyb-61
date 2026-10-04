first = float(input("Первое число: "))
second = float(input("Второе число: "))
operation = input("Операция (+, -, *, /): ")

if operation == "+":
    result = first + second
    print(f"Результат: {result:.2f}")
elif operation == "-":
    result = first - second
    print(f"Результат: {result:.2f}")
elif operation == "*":
    result = first * second
    print(f"Результат: {result:.2f}")
elif operation == "/":
    if second == 0:
        print("Деление на ноль запрещено")
    else:
        result = first / second
        print(f"Результат: {result:.2f}")
else:
    print("Неизвестная операция")