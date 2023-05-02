def decorator_(fn):
    def wrapper_(*args):
        for i, arg in enumerate(args):
            if type(arg) != int:
                raise TypeError(f'Аргумент {arg}, под индексом {i} не типа "int"')
        return fn(*args)
    return wrapper_

@decorator_
def multiply_a_b_c(a, b, c):
    return a * b * c



if __name__ == "__main__":
    print(multiply_a_b_c(1, 2, 3))
    multiply_a_b_c(1, "2", 3)
