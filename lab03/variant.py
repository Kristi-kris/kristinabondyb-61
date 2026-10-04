charge = int(input("Заполнение резервуара: "))

if charge < 0 or charge > 100:
    print("Ошибка диапазона")
elif charge <=24:
    print("Низкий")
elif charge <= 74:
    print("Средний")
else:
    print("Высокий")
