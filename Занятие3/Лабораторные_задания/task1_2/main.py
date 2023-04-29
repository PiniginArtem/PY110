OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "wt") as file:
        for i in range(10):
            file.write(("*" * (i + 1)).rjust(10, " ") + "\n")


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
