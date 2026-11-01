from functions import average, normalize_text, sum_digits, select_numbers

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

assert select_numbers([-5, 0, 2, 5], 2) == [-5]
assert select_numbers([], 2) == []
assert select_numbers([1, 2, 3], 2) == [1]
assert select_numbers([-5, -3, -1], 0) == [-5, -3, -1]
assert select_numbers([-5, -5, 3], 2) == [-5, -5]

print("Базовые проверки пройдены")