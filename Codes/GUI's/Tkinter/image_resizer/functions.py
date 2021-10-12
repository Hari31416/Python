from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image
import tkinter as tk

# Opening the file and returning its path
def show_image():
    global img
    global filepath
    filepath = askopenfilename(
        filetypes=[("Image Files", "*.png"), ("All Files", "*.*")]
    )
    img = Image.open(filepath)
    img = ImageTk.PhotoImage(img)
    lbl_image.config(image=img)


def show_resized_image():
    global resized_img
    raw_img = Image.open(filepath)
    height = int(ent_height.get())
    width = int(ent_width.get())
    resized_img = raw_img.resize((height, width))
    resized_img = ImageTk.PhotoImage(resized_img)
    lbl_image.config(image=resized_img)


def save_resized_image():
    pil_image = Image.open(filepath)
    height = int(ent_height.get())
    width = int(ent_width.get())
    resized_image = pil_image.resize((height, width))
    save_path = asksaveasfilename(
        filetypes=[("Image Files", "*.png"), ("All Files", "*.*")]
    )
    resized_image.save(f"{save_path}.png")
