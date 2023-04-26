def output_type_list(fn):
    def wrapper(*args, **kwargs):

        result = fn(*args, **kwargs)
        if not isinstance(result, list):  # Если результат оборачиваемой функции не дист, возвращает ошибку типа
            raise TypeError(f"Результатом выполнения функции {fn} должен быть список")
            # Декоратор не возвращает результат выполнения ф-ции
    return wrapper


@output_type_list
def return_list() -> list:
    return []


@output_type_list
def return_tuple() -> str:
    return ""


if __name__ == "__main__":
    return_list()
    return_tuple()
