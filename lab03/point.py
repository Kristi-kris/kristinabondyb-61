x = float(input("Координата x: "))
y = float(input("Координата y: "))

if 0 <= x <= 5 and 0 <= y <= 3:
    print("Внутри или на границе")
else:
    print("Снаружи")