import json


def task():
    filename = "input.json"  # имя файла "input.json"
    with open(filename) as f:  # открываем файл с именем "input.json" как "f"
        json_data = json.load(f)  # загружаем данные из файла "f" и именуем как объект "json_data"

    map_iterator = map(lambda item: item["score"] * item["weight"], json_data)  #
    # "map" создает итератор, применяя лямбду функцию ко всем объектам списка "json_data". Возвращает лямбду функцию,
    # которая принимает поочередно словарь из списка "json_data" и возвращает произведения "score" * "weight"

    return sum(map_iterator)  # Находим сумму произведений "score" * "weight"


if __name__ == "__main__":
    result = task()
    print(f"{result:.3f}")
