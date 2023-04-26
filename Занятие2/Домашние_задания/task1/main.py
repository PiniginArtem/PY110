def geometric_progression(factor: int = 2):
    """
    Функция-генератор геометрической прогрессии вида n = (n-1) * factor
    factor: целое число, больше 0
    """
    if factor < 1:
        raise ValueError("factor должно быть больше 0")
    number = 1
    yield number
    while True:
        number *= factor
        yield number

if __name__ == "__main__":
    geometric_progression_3 = geometric_progression(3)
    for num in geometric_progression_3:
        print(num)
        if num > 10000:
            break
