print ( "Введите число:")
def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

# Ввод числа и вывод результата
try:
    n = int(input().strip())
    if 0 < n < 4000:
        print(int_to_roman(n))
    else:
        print("Число должно быть в диапазоне 0 < n < 4000")
except ValueError:
    print("Ошибка: введите целое число")