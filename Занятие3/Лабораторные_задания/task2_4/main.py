import json


def task():
    filename = "input.json"
    with open(filename) as file_json:
        data = json.load(file_json)

    gen_exr = (i['contains_improvement_appeals'] for i in data)

    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
