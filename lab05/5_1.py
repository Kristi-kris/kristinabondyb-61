text = input("Введите текст: ")
normal = " ".join(text.split())

print(f"Исходная длина: {len(text)}")
print(f"Новая длина: {len(normal)}")
print(f"Нормализованный текст:{normal}")
print(f"Слов: {len(normal.split())}")