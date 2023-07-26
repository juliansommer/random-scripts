try:
    from ctypes import windll
    from PIL import Image
    from PIL.ExifTags import TAGS
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
    print("Open the file: ")
    filename = filedialog.askopenfilenames(filetypes=[("PNG", ".png"), ( "JPG", ".jpg")])

    if not len(filename) >= 1:  # they didnt select a folder
        print("Invalid File \n")
        main()

    image = Image.open(str("".join(filename)))

    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }

    for label,value in info_dict.items():
        print(f"{label:25}: {value}")

    exifdata = image.getexif()

    if not len(exifdata) >= 1:
        print("No exif data")
    else:
        for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")
            pass
main()