last_name = input("Фамилия: ")
first_name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст в полных годах: "))
favorite_subject = input("Любимый предмет: ")
study_hours = float(input("Часов подготовки в неделю: "))

if not 1 <= age <= 120:
	raise ValueError("Возраст должен быть от 1 до 120 лет")
if study_hours < 0:
	raise ValueError("Часы подготовки не могут быть отрицательными")

print("\nКарточка студента")
print(f"Имя: {first_name} {last_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст через четыре года: {age + 4}")
print(f"Любимый предмет: {favorite_subject}")
print(f"Подготовка за четыре недели: {study_hours * 4:.2f} ч")
print(f"В среднем за день семидневной недели: {study_hours / 7:.2f} ч")