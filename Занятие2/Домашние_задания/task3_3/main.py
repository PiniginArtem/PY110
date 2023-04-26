def arg_kwarg_isiter(fn):
    def wrapper_(*args, **kwargs):
        for i, arg in enumerate(args):
            try:
                (_ for _ in arg)
            except TypeError:
                raise TypeError(f"Объект {arg} под индексом {i} не является итерируемым")
        for key, arg in kwargs.items():
            try:
                (_ for _ in arg)
            except TypeError:
                raise TypeError(f"Объект {arg} под индексом {key} не является итерируемым")
        return fn(*args, **kwargs)
    return wrapper_


@arg_kwarg_isiter
def pow_list(a, b, keys):
    """
    Функция поочередно возводит число из первого списка в степень из второго списка
    и добавляет это значение в возвращаемый список если значение из keys = 1 или True
    """
    list_ = []
    for a_, b_, key in zip(a, b, keys):
        if key:
            list_.append(a_ ** b_)
    # filter((i != 0 for i in key), map(pow, a, b))
    return list_


if __name__ == "__main__":
    print(pow_list([2, 2, 2], [1, 2, 3], keys=[0, 1, 1]))
    pow_list(1, [1, 2, 3], keys=12)
