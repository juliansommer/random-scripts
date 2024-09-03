import tkinter as tk
from ctypes import windll
from tkinter import filedialog

windll.shcore.SetProcessDpiAwareness(1)  # fixes the blurry file dialog

root = tk.Tk()
root.withdraw()
root.attributes(
    "-topmost", True
)  # Opened window will be above all other windows even if clicked off


def open_file() -> str:
    print("Open the Number List")
    filename = filedialog.askopenfilenames(filetypes=[("Text", ".txt")])

    # if you do not select a file the first time, then select one, theres some error so just exit
    if len(filename) < 1:
        print("Invalid File\n")
        exit()

    return "".join(filename)


def clean_file(filename: str) -> list:
    with open(filename, "r") as f:
        startlist = f.readlines()
        startlist = [x.strip() for x in startlist]  # removes spaces
    return startlist


def find_prime(startlist: list) -> list:
    prime = []
    nonprime = []
    for i in startlist:
        try:
            if int(i) > 1:
                for x in range(2, int(i)):
                    if (int(i) % x) == 0:
                        nonprime.append(
                            i + " (" + str(x) + "\u00d7" + str(int(i) // x) + ")"
                        )
                        break
                else:
                    prime.append(i)
            else:  # num is 0 or  1
                nonprime.append(i)
        except ValueError:  # if there is a letter in document
            pass

    return prime, nonprime


def main() -> None:
    prime = []
    nonprime = []
    filename = open_file()
    startlist = clean_file(filename)
    prime, nonprime = find_prime(startlist)

    if len(prime) == 0:
        print("No Prime Numbers")
    else:
        print("Prime Numbers:", ", ".join(sorted(prime, key=int)))

    if len(nonprime) == 0:
        print("No Non Prime Numbers")
    else:
        print(
            "Non Prime Numbers:",
            ", ".join(sorted(nonprime, key=lambda x: int(x.split()[0]))),
        )


if __name__ == "__main__":
    main()
