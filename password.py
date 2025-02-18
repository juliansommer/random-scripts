from secrets import choice
from string import ascii_letters, digits, punctuation

import pyperclip as pc


def password_generator(length: int) -> str:
    return "".join(choice(ascii_letters + digits + punctuation) for _ in range(length))


def main() -> None:
    try:
        length = int(input("How long do you want the password to be? "))
    except ValueError:
        print("Please enter a valid number.")
        exit()

    password = password_generator(length)
    pc.copy(password)
    print(f"Password: {password} has been copied to clipboard.")
    exit()


if __name__ == "__main__":
    main()
