first_text = "2"
second_text = "3"
print(f"А, до преобразования: {type(first_text).__name__}, {type(second_text).__name__}")
first_number = int(first_text)
second_number = int(second_text)
print(f"А, после преобразования: {type(first_number).__name__}, {type(second_number).__name__}")
print(f"А, сумма: {first_number + second_number}")

age_text = input("Возраст для фрагмента Б: ")
print(f"Б, до преобразования: {type(age_text).__name__}")
age = int(age_text)
print(f"Б, после преобразования: {type(age).__name__}")
print(f"Б, возраст через год: {age + 1}")

first = 4
second = 7
third = 10
average = (first + second + third) / 3
print(f"В, среднее трёх чисел: {average}")