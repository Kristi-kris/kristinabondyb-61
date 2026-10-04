first_subject = input("Первый предмет: ")
first_lessons = int(input("Занятий по первому предмету за неделю: "))
first_minutes = int(input("Минут в одном занятии: "))
second_subject = input("Второй предмет: ")
second_lessons = int(input("Занятий по второму предмету за неделю: "))
second_minutes = int(input("Минут в одном занятии: "))
available_hours = float(input("Доступно часов на неделю: "))

if first_lessons < 0 or second_lessons < 0:
	raise ValueError("Количество занятий не может быть отрицательным")
if first_minutes <= 0 or second_minutes <= 0:
	raise ValueError("Продолжительность занятия должна быть положительной")

first_total = first_lessons * first_minutes
second_total = second_lessons * second_minutes
weekly_total = first_total + second_total
weekly_hours = weekly_total / 60

if available_hours < weekly_hours:
	raise ValueError("Доступного времени меньше суммарной нагрузки")

print(f"{first_subject}: {first_total} мин")
print(f"{second_subject}: {second_total} мин")
print(f"Общая нагрузка: {weekly_total} мин ({weekly_hours:.2f} ч)")
print(f"Свободное время: {available_hours - weekly_hours:.2f} ч")
print(f"Нагрузка за четыре недели: {weekly_hours * 4:.2f} ч")