def positive_check(fn):
    def wrapper(arg):
        if arg >= 0:
            print("всё хорошо")
        else:
            raise ValueError("число должно быть >= 0")

        result = fn(arg)
        return result

    return wrapper


@ positive_check
def some_func(num: int):
    ...


if __name__ == "__main__":
    some_func(5)  # всё хорошо

    some_func(-5)  # должна быть вызвана ошибка ValueError
