import json


def task():
    filename = "input.json"
    with open(filename) as f:
        data = json.load(f)

    return max(data, key=lambda data_list: data_list['score'])


if __name__ == "__main__":
    print(task())
