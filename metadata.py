import tkinter as tk
from ctypes import windll
from tkinter import filedialog

from PIL import Image as PILImage
from PIL.ExifTags import TAGS

windll.shcore.SetProcessDpiAwareness(1)  # fixes the blurry file dialog

root = tk.Tk()
root.withdraw()
root.attributes(
    "-topmost", True
)  # Opened window will be above all other windows even if clicked off


def select_image() -> str:
    print("Open The Image")
    filename = filedialog.askopenfilenames(filetypes=[("PNG", ".png"), ("JPG", ".jpg")])

    # if you do not select a file the first time, then select one, theres some error so just exit
    if len(filename) < 1:
        print("Invalid File\n")
        exit()

    return "".join(filename)


def image_data(image: PILImage.Image, filename: str) -> None:
    info_dict = {
        "Filename": filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1),
    }

    print("\nImage Information")
    for label, value in info_dict.items():
        print(f"{label:25}: {value}")


def exif_data(image: PILImage.Image) -> None:
    exif = image.getexif()

    if not len(exif) < 1:
        print("\nEXIF Data:")
        for tag_id in exif:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exif.get(tag_id)
            # decode bytes
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")


def main() -> None:
    filename = select_image()
    image = PILImage.open(filename)
    image_data(image, filename)
    exif_data(image)


if __name__ == "__main__":
    main()
