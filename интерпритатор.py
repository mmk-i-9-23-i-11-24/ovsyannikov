print("Введите выражение: ")
expression = input().strip().split() # Чтение ввода

if len(expression) != 3:
    print("Ошибка: введите выражение в формате 'a operator b'") # Проверка корректности ввода
    exit()

a_chislo, op, b_chislo = expression

try:# Проверка, что a и b — числа
    a = int(a_chislo)
    b = int(b_chislo)
except ValueError:
    print("Ошибка: a и b должны быть целыми числами") # Выводит ошибку если если числ не целые
    exit()


if not (0 <= a <= 1000 and 0 <= b <= 1000): # Проверка диапазона (0 ≤ a, b ≤ 1000)
    print("Ошибка: числа должны быть в диапазоне 0 ≤ a, b ≤ 1000")
    exit()


if op == "plus": # Вычисление результата в зависимости от оператора
    resultat = a + b
elif op == "minus":
    resultat = a - b
elif op == "multiply":
    resultat = a * b
elif op == "divide":
    if b == 0:
        print("Ошибка: деление на ноль")
        exit()
    resultat = a // b  # Целочисленное деление
else:
    print("Ошибка: неизвестный оператор. Используйте plus, minus, multiply, divide")
    exit()

# Вывод результата
print(resultat)