import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter.messagebox import showerror

# Functions
# Showing the Image
def show_image():
    """Opens the file manager to ask for a image then shows it."""
    global img
    global filepath
    filepath = askopenfilename(
        filetypes=[("Image Files", "*.png"), ("All Files", "*.*")]
    )
    img = Image.open(filepath)
    img = ImageTk.PhotoImage(img)
    lbl_image.configure(background="red")
    lbl_image.config(image=img)


def show_resized_image():
    """Shows the resized image"""
    global resized_img
    try:
        raw_img = Image.open(filepath)
        height = int(ent_height.get())
        width = int(ent_width.get())
        resized_img = raw_img.resize((width, height))
        resized_img = ImageTk.PhotoImage(resized_img)
        lbl_image.config(image=resized_img)
    except NameError:
        showerror("NO IMAGE", "No image selected!")
    except ValueError:
        showerror("INVALID DIMENSIONS", "Please Provide a Valid Height and Width")
    except AttributeError:
        showerror("NO IMAGE", "No image selected!")


def save_resized_image():
    """Saves the resized image"""
    try:
        pil_image = Image.open(filepath)
        height = int(ent_height.get())
        width = int(ent_width.get())
        resized_image = pil_image.resize((width, height))
        save_path = asksaveasfilename(
            filetypes=[("Image Files", "*.png"), ("All Files", "*.*")]
        )
        resized_image.save(f"{save_path}.png")
    except NameError:
        showerror("NO IMAGE", "No image selected!")
    except AttributeError:
        showerror("NO IMAGE", "No image selected!")
    except ValueError:
        showerror("INVALID DIMENSIONS", "Please Provide a Valid Height and Width")


# Setting Windows
background_color = "#d3f4f5"
window = tk.Tk()
window.title("Simple Image Resizer")
window.configure(background=background_color)
window.rowconfigure(1, weight=1, minsize=500)
window.columnconfigure(2, weight=1, minsize=800)

# The Frames
# Input Frame
frm_input = tk.Frame(window)
frm_input.rowconfigure(1, weight=1, minsize=50)
frm_input.configure(background=background_color)
frm_input.grid(row=0, column=0, sticky="", columnspan=3, pady=10)

# Buttons Frames
frm_buttons = tk.Frame(window)
frm_buttons.configure(background=background_color)
frm_buttons.rowconfigure(3, weight=1, minsize=100)
frm_buttons.columnconfigure(1, weight=1, minsize=45)
frm_buttons.grid(row=1, column=0, sticky="", rowspan=2)

# Image Frame
frm_image = tk.Frame(window)
frm_image.configure(background=background_color)
frm_image.grid(row=1, column=1, sticky="nsew", columnspan=2, rowspan=2)

# Input Entry Widgets and Labels
# The Labels
lbl_height = tk.Label(
    frm_input, text="Height", font=("Arial", 14), padx=5, bg=background_color
)
lbl_height.grid(row=0, column=0, sticky="")
lbl_width = tk.Label(
    frm_input, text="Width", font=("Arial", 14), padx=5, bg=background_color
)
lbl_width.grid(row=1, column=0, sticky="")
# The Entries
ent_height = tk.Entry(frm_input, bg=background_color, borderwidth=3)
ent_height.grid(row=0, column=1, sticky="")
ent_width = tk.Entry(frm_input, bg=background_color, borderwidth=3)
ent_width.grid(row=1, column=1, sticky="")

# Buttons
# Open Button
btn_open = tk.Button(
    frm_buttons,
    text="Open",
    relief=tk.RAISED,
    borderwidth=5,
    font=("Arial", 13),
    bg=background_color,
    command=show_image,
)
btn_open.grid(row=0, column=0, sticky="ns", ipadx=5, ipady=5, padx=10, pady=5)
# Show Resized Image Button
btn_show = tk.Button(
    frm_buttons,
    text="Resize",
    font=("Arial", 13),
    relief=tk.RAISED,
    borderwidth=5,
    bg=background_color,
    command=show_resized_image,
)
btn_show.grid(row=1, column=0, sticky="ns", ipadx=5, ipady=5, padx=10, pady=5)
# Save Resized Image Button
btn_resize = tk.Button(
    frm_buttons,
    text="Save Resized Image",
    font=("Arial", 13),
    relief=tk.RAISED,
    borderwidth=5,
    bg=background_color,
    command=save_resized_image,
)
btn_resize.grid(row=2, column=0, sticky="ns", ipadx=5, ipady=5, padx=10, pady=5)
# Quit Button
btn_quit = tk.Button(
    frm_buttons,
    text="Quit",
    font=("Arial", 13),
    relief=tk.RAISED,
    borderwidth=5,
    bg=background_color,
    command=window.destroy,
)
btn_quit.grid(row=3, column=0, sticky="ns", padx=10, pady=5)

# The Image
lbl_image = tk.Label(frm_image)
lbl_image.configure(background=background_color)
lbl_image.grid(row=0, column=0, sticky="nsew")

# Run the app
if __name__ == "__main__":
    window.mainloop()
