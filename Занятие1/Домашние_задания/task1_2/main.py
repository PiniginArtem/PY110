from itertools import repeat


def task(list_args: list) -> bool:  # True, если все числа целые; False, если любой элемент другого типа
    return all(map(isinstance, list_args, repeat(int)))  # Проверяет, являются ли все элементы списка целыми числами


if __name__ == "__main__":
    print(task([1, 2, 3]))   # True
    print(task(["str", 2, 3]))  # False
