import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r'#{4} (?P<position>\d{1,2})\. \[(?P<book>.+?)\]\((?P<book_url>.+?)\) by (?P<author>.+?)\(' \
             r'(?P<recommended>.+?\%) recommended\).+?\((?P<cover_url>.+?)\).+?\"(?P<description>.+?)\"'


def find_info() -> list[dict]:
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)
    list_dict = []
    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            data = book.groupdict()
            list_dict.append(data)
            print(json.dumps(data, indent=4))
    return list_dict


def write_file(data: list[dict], output_filename: str):
    with open(output_filename, "w") as out_f:
        json.dump(data, out_f, indent=4)


def sorted_list_dict(data: list[dict]) -> list[dict]:
    return sorted(data, key=lambda x: x["position"])


if __name__ == "__main__":
    file = "output.json"
    write_file(sorted_list_dict(find_info()), file)
