from string import ascii_lowercase, ascii_uppercase, digits
from random import sample


def password_generator(len_password: int = 8):
    alphabet = ascii_lowercase + ascii_uppercase + digits
    while True:
        password = "".join(sample(alphabet, len_password))
        yield password


if __name__ == "__main__":
    for i in range(3):
        print(next(password_generator(14)))
