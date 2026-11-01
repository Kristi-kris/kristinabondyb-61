# Лабораторная работа 7.

## Файлы:

* functions.py
* main.py
* test\_functions.py
* README.md

## Команды запуска

* python main.py — демонстрация работы функций.
* python test\_functions.py — запуск автоматических проверок.

## Проверки функций

|Вход|Ожидаемый результат|Результат|
|-|-|-|
|sum\_digits(0)|0|0|
|sum\_digits(507)|12|12|
|sum\_digits(-507)|12|12|
|average(\[])|None|None|
|average(\[2, 4, 6])|4|4|
|normalize\_text("  ПРИВЕТ   Мир  ")|«привет мир»|«привет мир»|
|normalize\_text("   ")|«»|«»|

## variant.py — вариант 13



|Вход|Ожидаемый результат|Результат|
|-|-|-|
|select\_numbers(\[-5, 0, 2, 5], 2)|\[-5]|\[-5]|
|select\_numbers(\[], 2)|\[]|\[]|
|select\_numbers(\[1, 2, 3], 2)|\[1]|\[1]|
|select\_numbers(\[-5, -3, -1], 0)|\[-5, -3, -1]|\[-5, -3, -1]|
|select\_numbers(\[-5, -5, 3], 2)|\[-5, -5]|\[-5, -5]|



