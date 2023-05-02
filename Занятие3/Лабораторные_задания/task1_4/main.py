INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) as inp_file:
        with open(OUTPUT_FILE, "w") as outp_file:
            for line_wt in map(str.upper, inp_file):
                outp_file.write(line_wt)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
