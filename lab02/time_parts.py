total_seconds = int(input("Общее количество секунд: "))

if total_seconds < 0:
	raise ValueError("Количество секунд не может быть отрицательным")

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours} ч {minutes} мин {seconds} с")