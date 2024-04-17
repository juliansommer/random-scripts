import string
import random

def main():
    password = []

    length = int(input("Enter the length of the password: "))
    symbols = input("Do you want to use symbols? y/n ")

    if symbols.lower() == "y":
        characters = list(string.ascii_letters + string.digits + string.punctuation)
    elif symbols.lower() != "y":
        characters = list(string.ascii_letters + string.digits)

    for _ in range(length):
        password.append(random.choice(characters))

    print("".join(password))

    save = input("Do you want to save the password to a text document? ")
    if save.lower() == "y" or save.lower() == "yes":
        with open("savedpasswords.txt","a+") as f:
            f.write("".join(password))
            f.write("\n")
            print("Password saved to savedpasswords.txt")


if __name__ == "__main__":
    main()
