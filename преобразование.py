print("Введите число которое нужно преобразовать:")
mapping = {
    'mile': 1609,
    'yard': 0.9144,
    'foot': 0.3048,
    'inch': 0.0254,
    'km': 1000,
    'm': 1,
    'cm': 0.01,
    'mm': 0.001
}

try:
    inp = input().split()
    if len(inp) != 4:
        raise ValueError("Нужен ввод в формате: <число> <из_единицы> to <в_единицы>") # Выводит ошбику о не рпавильно формате

    value = float(inp[0])  # Если не число — вызовет ValueError
    from_unit = inp[1]
    to_unit = inp[3]

    if from_unit not in mapping or to_unit not in mapping:
        raise ValueError("Неподдерживаемая единица измерения")

    result = value * mapping[from_unit] / mapping[to_unit]
    print("ваше число: "+'%.2e' % result )

except ValueError as e:
    print(f"Ошибка: {e}")