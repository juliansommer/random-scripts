import os
import pathlib
import tkinter as tk
from ctypes import windll
from tkinter import filedialog
from typing import List

windll.shcore.SetProcessDpiAwareness(1)  # fixes the blurry file dialog

root = tk.Tk()
root.withdraw()
root.attributes(
    "-topmost", True
)  # Opened window will be above all other windows even if clicked off


def open_folder() -> str:
    path_input = filedialog.askdirectory()

    # if you do not select a folder the first time, then select one, theres some error so just exit
    if len(path_input) < 1:
        print("Invalid Folder\n")
        exit()

    return path_input


def rename_files(path_input: str, full_list: List[str], name_input: str) -> None:
    for i in range(len(full_list)):
        extension = pathlib.Path(full_list[i]).suffix
        source = os.path.join(path_input, full_list[i])
        destination = os.path.join(path_input, (name_input + str(i) + extension))
        print(f"{source} -> {destination}")
        os.rename(source, destination)


def main() -> None:
    path_input = open_folder()

    name_list = os.listdir(path_input)
    name_input = input("What do you want the files to be renamed to? ")

    full_list = [os.path.join(path_input, i) for i in name_list]
    rename_files(path_input, full_list, name_input)


if __name__ == "__main__":
    main()
