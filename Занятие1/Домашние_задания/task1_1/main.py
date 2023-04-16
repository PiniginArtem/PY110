import itertools


def enumerate_zip(list_variable):
    return zip(itertools.count(), list_variable)

if __name__ == "__main__":
    a = ["a", "b", "c", "d", "e", "f"]
    for i, letter in enumerate_zip(a):
        print(f"Для буквы {letter} соотвествует индекс {i}")

