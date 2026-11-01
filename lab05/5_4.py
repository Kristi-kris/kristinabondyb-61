text = input("Введите строку: ")
words = text.split()

count = 0
for word in words:
    cleaned = word.strip(".,!?;:").lower()
    if cleaned and cleaned.endswith("а"):
        print(cleaned)
        count += 1

if count == 0:
    print("Нет совпадений")
print(f"Количество: {count}")
