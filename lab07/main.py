from functions import sum_digits, average, normalize_text, select_numbers

number = int(input("Введите целое число: "))
print(f"Сумма цифр: {sum_digits(number)}")

parts = input("Введите целые числа через пробел: ").split()
numbers = [int(p) for p in parts]

avg = average(numbers)
if avg is None:
    print("Среднее: Нет данных")
else:
    print(f"Среднее: {avg:.2f}")

text = input("Введите текст: ")
print(f"Нормализованный текст: {normalize_text(text)}")

threshold = int(input("Введите порог: "))
print(f"Выборка: {select_numbers(numbers, threshold)}")