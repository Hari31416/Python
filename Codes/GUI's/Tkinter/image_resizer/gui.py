# Making an app to resize images using tkinter
import tkinter as tk
from functions import *

window = tk.Tk()
window.title("Image Resizer")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
# Frame
frm_btn = tk.Frame(window)
frm_btn.grid(row=0, column=0, sticky="ns")

# The Canvas
cnv_image = tk.Canvas(window)
cnv_image.grid(row=0, column=1, sticky="nsew")


# The buttons
btn_open = tk.Button(frm_btn, text="Open", command=open_file)
btn_save = tk.Button(frm_btn, text="Save", command=save_file)
btn_open.grid(row=0, column=0, sticky="ew")
btn_save.grid(row=1, column=0, sticky="ew")

window.mainloop()
