total_volume = int(input("количество участников: "))
capacity = int(input("количество участников в команде: "))

full_units = total_volume // capacity
remainder = total_volume % capacity
units_needed = (total_volume + capacity - 1) // capacity

print(f"Полностью заполненных единиц: {full_units}")
print(f"Остаток: {remainder}")
print(f"Всего единиц нужно: {units_needed}")
