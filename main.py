from conf import MODEL
from faker import Faker
import json
import random


def get_title() -> str:
    """
    Возвращает случайное название книги из файла books.txt, где каждое название записано с новой строки
    """
    file_path = "books.txt"
    with open(file_path, encoding='utf-8') as books:
        data = []
        for line in books:
            data.append(line[:-1])
        return random.choice(data)


def character_count_check(character_count: int):
    """
    Фабрика декоратора, которая на вход принимает целое число (кол-во символов)
    и проверяет меньше ли по длине результат оборачиваемой ф-ции.
    Если больше или равно, то инициализирует ValueError.
    """
    def my_decorator(fun):
        def wrapper(*ar, **kw):
            book_title = fun(*ar, **kw)
            if len(book_title) >= character_count:
                raise ValueError(f"Название книги должно быть меньше {character_count}")
            return book_title
        return wrapper
    return my_decorator


@character_count_check(30)
def get_title_2() -> str:
    """
    Возвращает случайное название книги из файла books.txt, где каждое название записано с новой строки
    """
    file_path = "books.txt"
    with open(file_path, "rb") as books:
        data = [0, ]
        i = 0
        while True:
            book = books.readline()
            if not book:
                break
            data.append(len(book) + data[i])
            i += 1
        random_number = random.randint(1, data[-1])
        for i in range(len(data) - 1):
            if data[i] < random_number <= data[i + 1]:
                books.seek(data[i], 0)
                return books.read(data[i + 1] - data[i]).decode('utf-8')[:-2]


def get_year(from_: int = 0, to_: int = 2023) -> int:
    """
    Возвращает случайное целое число, по умолчанию от 0 до 2023
    """
    return random.randint(from_, to_)


def get_pages(from_: int = 0, to_: int = 300) -> int:
    """
    Возвращает случайное целое число, по умолчанию от 0 до 300
    """
    return random.randint(from_, to_)


def get_isbn13() -> str:
    """
    Возвращает индекс "isbn13" генерируемый случайным образом
    """
    Faker.seed()
    return Faker().isbn13()


def get_rating(from_: int = 0, to_: int = 5) -> float:
    """
    Возвращает случайное число с плавающей точкой, A ≤ N ≤ B (или B ≤ N ≤ A)
    """
    return random.uniform(from_, to_)


def get_price(from_: int = 0, to_: int = 10000) -> float:
    """
    Случайное число с плавающей точкой, A ≤ N ≤ B (или B ≤ N ≤ A), округленное до 2ого знака после запятой
    """
    return round(random.uniform(from_, to_), 2)


def get_author() -> list:
    """
    Генерирует список, в котором находится случайное кол-во (от 1 до 3 включительно) случайно сгенерированных ФИО
    """
    data = []
    fake = Faker("ru_RU")
    for _ in range(random.randint(1, 3)):
        data.append(fake.name())
    return data


def generate_dict_book(start_number: int = 1):
    """
    Функция-генератор, который возвращает словарь книги
    """
    count_ = start_number
    while True:
        try:
            title_ = get_title_2()
            yield {
                "model": MODEL,
                "pk": count_,
                "fields": {
                    "title": title_,
                    "year": get_year(),
                    "pages": get_pages(),
                    "isbn13": get_isbn13(),
                    "rating": get_rating(),
                    "price": get_price(0, 20000),
                    "author": get_author()
                }
            }
            count_ += 1
        except ValueError:
            print("Отсеяно название книги, словарь не будет сгенерирован")
            yield None


def main(start_number: int = 1, number_of_times: int = 100):
    gen_func = generate_dict_book(start_number)
    filename = "books_out.json"
    with open(filename, "w", encoding='utf-8') as f:
        count_ = start_number
        end_pos = number_of_times + start_number
        while count_ != end_pos:
            data = next(gen_func)
            if data:
                json.dump(data, f, indent=4, ensure_ascii=False)
                if count_ != end_pos - 1:
                    f.write(",\n")
                count_ += 1


if __name__ == "__main__":
    main(24, 10)
