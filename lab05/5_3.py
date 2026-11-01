text = input("Введите текст: ")
count = text.count(":")
new = text.replace(":", "-")

print(f"Замен: {count}")
print(new)