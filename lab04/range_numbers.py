start = int(input("Начало диапазона: "))
end = int(input("Конец диапазона: "))

if start <= end:
    for number in range(start, end + 1):
        print(number)
else:
    for number in range(start, end - 1, -1):
        print(number)