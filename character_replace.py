import os
import tkinter as tk
from ctypes import windll
from itertools import product
from tkinter import filedialog

windll.shcore.SetProcessDpiAwareness(1)  # fixes the blurry file dialog

root = tk.Tk()
root.withdraw()
root.attributes(
    "-topmost", True
)  # Opened window will be above all other windows even if clicked off

OPTIONS = {
    "a": ["a", "4", "@"],
    "A": ["A", "4", "@"],
    "b": ["b", "8"],
    "B": ["B", "8"],
    "e": ["e", "3"],
    "E": ["E", "3"],
    "g": ["g", "9"],
    "G": ["G", "9"],
    "i": ["i", "1", "!"],
    "I": ["I", "1", "!"],
    "l": ["l", "1"],
    "L": ["L", "1"],
    "o": ["o", "0"],
    "O": ["O", "0"],
    "s": ["s", "5", "$"],
    "S": ["S", "5", "$"],
    "t": ["t", "7"],
    "T": ["T", "7"],
    "z": ["z", "2"],
    "Z": ["Z", "2"],
}


def select_file() -> str:
    print("Open the Word List")
    filename = filedialog.askopenfilenames(filetypes=[("Text", ".txt")])

    # for whatever reaason, if you do not select a file the first time, then select one, theres some error so just exit
    if len(filename) < 1:
        print("Invalid File")
        exit()

    return "".join(filename)


def read_file(filename: str) -> list:
    with open(filename, "r") as f:
        startlist = f.readlines()
        return [x.strip() for x in startlist]


def save_file(filename: str, startlist: list) -> None:
    with open(filename, "w+") as f:
        for word in startlist:
            for newword in filler(word):
                final_word = "".join(newword) + "\n"
                f.write(final_word)
    print(f"Saved to {os.getcwd()}\\{filename}")


def filler(word: str) -> list:
    combos = [(c,) if c not in OPTIONS else OPTIONS[c] for c in word]
    return list(("".join(o) for o in product(*combos)))


def main() -> None:
    filename = select_file()
    startlist = read_file(filename)
    save_file("NewList.txt", startlist)


if __name__ == "__main__":
    main()
