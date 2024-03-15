try:
    import os
    from ctypes import windll
    from itertools import product
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import tkFileDialog as filedialog

windll.shcore.SetProcessDpiAwareness(1) # fixes the blurry file dialog

root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True) # Opened window will be above all other windows even if clicked off

options = {
    "a": ["a", "4", "@"],
    "A": ["A", "4", "@"],
    "b": ["b", "8",],
    "B": ["B", "8",],
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
    "Z": ["Z", "2"]}

def filler(word):
    combos = [(c,) if c not in options else options[c] for c in word]
    return ("".join(o) for o in product(*combos))

def main():
    print("Open the Word List")
    filename = filedialog.askopenfilenames(filetypes=[("Text", ".txt")])

    if not len(filename) >= 1:  # they didn't select a file
        print("Invalid File \n")
        main()

    with open("".join(filename), "r") as f:
        startlist = f.readlines()
        startlist = [x.strip() for x in startlist]  # removes spaces

    with open("NewList.txt","w+") as f:  # writes over file
        for word in startlist:
            temp_list = list(filler(word))
            for newword in temp_list:
                f.write("".join(newword) + "\n")

    with open("NewList.txt", "r") as f:
        endlist = f.readlines()
        endlist = [x.strip() for x in endlist]

    directory_path = os.getcwd()
    print("Saved to " + directory_path + "\\NewList.txt")

if __name__ == "__main__":
    main()
