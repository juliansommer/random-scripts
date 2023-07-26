try:
    import os
    from ctypes import windll
    import pathlib
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import tkFileDialog as filedialog

windll.shcore.SetProcessDpiAwareness(1)  # fixes the blurry file dialog

root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True) # Opened window will be above all other windows even if clicked off

def main():
    print("Open the file location: ")
    pathinput = filedialog.askdirectory()

    if not len(pathinput) >= 1:  # they didnt select a folder
        print("Invalid Folder \n")
        main()

    name_list = os.listdir(pathinput)
    nameinput = input("What do you want the files to be renamed to? ")

    full_list = [os.path.join(pathinput, i) for i in name_list]
    #sorted_list = sorted(full_list, key=lambda x: os.path.getctime(x))

    for i in range(len(full_list)):
        extension = pathlib.Path(full_list[i]).suffix
        print(full_list[i])
        source = os.path.join(pathinput, full_list[i])
        destination = os.path.join(pathinput, (nameinput + str(i) + extension))
        os.rename(source, destination)

main()