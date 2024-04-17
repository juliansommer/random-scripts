try:
    from ctypes import windll
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import tkFileDialog as filedialog

windll.shcore.SetProcessDpiAwareness(1)  # fixes the blurry file dialog

root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)  # Opened window will be above all other windows even if clicked off

prime = []
nonprime = []


def main():
    print("Open the Number List")
    filename = filedialog.askopenfilenames(filetypes=[("Text", ".txt")])

    if len(filename) < 1:  # they didnt select a file
        print("Invalid File \n")
        main()

    with open("".join(filename), "r") as f:
        startlist = f.readlines()
        startlist = [x.strip() for x in startlist]  # removes spaces

    for i in startlist:
        try:
            if int(i) > 1:
                for x in range(2, int(i)):
                    if (int(i) % x) == 0:
                        nonprime.append(i + " (" + str(x) + u"\u00D7" + str(int(i) // x) + ")")
                        break
                else:
                    prime.append(i)
            else:  # num is 0 or  1
                nonprime.append(i)
        except ValueError:  # if there is a letter in document
            pass

    prime = sorted(prime)
    prime = sorted(nonprime)

    if len(prime) == 0:
        print("No Prime Numbers")
    else:
        print("Prime Numbers:", ", ".join(prime))

    if len(nonprime) == 0:
        print("No Non Prime Numbers")
    else:
        print("Non Prime Numbers:", ", ".join(nonprime))


if __name__ == "__main__":
    main()
