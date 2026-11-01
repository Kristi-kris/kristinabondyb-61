text = input("Введите текст: ")
clean = text.lower().replace(" ", "")

if not clean:
    print("Нет текста")
elif clean == clean[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")