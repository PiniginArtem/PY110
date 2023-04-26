def flatten(list_of_lists: list[list[any]]):  # функция-генератор для вывода каждого элемента массива
    for inside_list in list_of_lists:  # пробегается по элементам верхнего list 1ый [1, 2, 3], 2ой [4, 5, 6] и тд
        for value in inside_list:  # пробегается по элементам вложенного list 1, 2, 3
            yield value  # возвращает каждый элемент с остановкой


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for ceil in flatten(matrix):  # вызывает поочерёдно элементы генератора от исходного list[list[]]
        print(ceil)
