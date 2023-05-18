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
    Cлучайное число с плавающей точкой, A ≤ N ≤ B (или B ≤ N ≤ A), округленное до 2ого знака после запятой
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


def generate_dict_book(start_number: int = 1) -> dict:
    """
    Функция-генератор, который возвращает словарь книги
    """
    while True:
        yield {
            "model": MODEL,
            "pk": start_number,
            "fields": {
                "title": get_title(),
                "year": get_year(),
                "pages": get_pages(),
                "isbn13": get_isbn13(),
                "rating": get_rating(),
                "price": get_price(0, 20000),
                "author": get_author()
            }
        }


def main(start_number: int = 1):
    data = []
    for i in range(start_number, start_number + 100):
        data.append(next(generate_dict_book(i)))
    filename = "books_out.json"
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
