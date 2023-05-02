import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    return sorted(json_data, key=lambda x: x["length"])


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

    output_filename = "output.json"
    with open(output_filename, "w") as file:
        json.dump(data, file, indent=2)
