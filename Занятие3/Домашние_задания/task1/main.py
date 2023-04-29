def list_generator(len_list: int = 10, len_item: int = 10) -> list:
    return ["".join([str(k) for k in range(len_item)]) + "\n" for _ in range(len_list)]


def write_file(file_name: str, data):
    with open(file_name, "w") as file:
        file.writelines(data)


def sum_files(name_1: str, name_2: str, name_3: str):
    with open(name_1) as file_1:
        with open(name_2) as file_2:
            with open(name_3, "w") as file_3:
                while True:
                    line = file_1.readline().strip() + file_2.readline().strip()
                    file_3.write(line + "\n")
                    if not line:
                        break


if __name__ == "__main__":
    write_file("file_1.txt", list_generator())
    write_file("file_2.txt", list_generator(len_item=20))
    sum_files("file_1.txt", "file_2.txt", "file_3.txt")
