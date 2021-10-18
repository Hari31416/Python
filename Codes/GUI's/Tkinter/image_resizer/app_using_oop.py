import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter.messagebox import showerror


class ImageResizer:
    def __init__(self):
        self.background_color = "#98faef"
        self.window = tk.Tk()
        self.window.title("Simple Image Resizer")
        self.window.configure(background=self.background_color)
        self.window.rowconfigure(1, weight=1, minsize=500)
        self.window.columnconfigure(2, weight=1, minsize=800)

    def create_frames(self):
        # Input Frame
        self.frm_input = tk.Frame(self.window)
        self.frm_input.rowconfigure(1, weight=1, minsize=50)
        self.frm_input.configure(background=self.background_color)
        self.frm_input.grid(row=0, column=0, sticky="", columnspan=3, pady=10)

        # Buttons Frames
        self.frm_buttons = tk.Frame(self.window)
        self.frm_buttons.configure(background=self.background_color)
        self.frm_buttons.rowconfigure(3, weight=1, minsize=100)
        self.frm_buttons.columnconfigure(1, weight=1, minsize=45)
        self.frm_buttons.grid(row=1, column=0, sticky="", rowspan=2)

        # Image Frame
        self.frm_image = tk.Frame(self.window)
        self.frm_image.configure(background=self.background_color)
        self.frm_image.grid(row=1, column=1, sticky="nsew", columnspan=2, rowspan=2)

    def create_input_tools(self):
        # The Labels
        self.lbl_height = tk.Label(
            self.frm_input,
            text="Height",
            font=("Arial", 14),
            padx=5,
            bg=self.background_color,
        )
        self.lbl_height.grid(row=0, column=0, sticky="")
        self.lbl_width = tk.Label(
            self.frm_input,
            text="Width",
            font=("Arial", 14),
            padx=5,
            bg=self.background_color,
        )
        self.lbl_width.grid(row=1, column=0, sticky="")
        # The Entries
        self.ent_height = tk.Entry(
            self.frm_input, bg=self.background_color, borderwidth=3
        )
        self.ent_height.grid(row=0, column=1, sticky="")
        self.ent_width = tk.Entry(
            self.frm_input, bg=self.background_color, borderwidth=3
        )
        self.ent_width.grid(row=1, column=1, sticky="")

    def create_buttons(self):
        # Open Button
        self.btn_open = tk.Button(
            self.frm_buttons,
            text="Open",
            relief=tk.RAISED,
            borderwidth=5,
            font=("Arial", 13),
            bg=self.background_color,
            command=self.show_image,
        )
        self.btn_open.grid(
            row=0, column=0, sticky="ns", ipadx=5, ipady=5, padx=10, pady=5
        )
        # Show Resized Image Button
        self.btn_show = tk.Button(
            self.frm_buttons,
            text="Resize",
            font=("Arial", 13),
            relief=tk.RAISED,
            borderwidth=5,
            bg=self.background_color,
            command=self.show_resized_image,
        )
        self.btn_show.grid(
            row=1, column=0, sticky="ns", ipadx=5, ipady=5, padx=10, pady=5
        )
        # Save Resized Image Button
        self.btn_resize = tk.Button(
            self.frm_buttons,
            text="Save Resized Image",
            font=("Arial", 13),
            relief=tk.RAISED,
            borderwidth=5,
            bg=self.background_color,
            command=self.save_resized_image,
        )
        self.btn_resize.grid(
            row=2, column=0, sticky="ns", ipadx=5, ipady=5, padx=10, pady=5
        )
        # Quit Button
        self.btn_quit = tk.Button(
            self.frm_buttons,
            text="Quit",
            font=("Arial", 13),
            relief=tk.RAISED,
            borderwidth=5,
            bg=self.background_color,
            command=self.window.destroy,
        )
        self.btn_quit.grid(row=3, column=0, sticky="ns", padx=10, pady=5)
        # The Image
        self.lbl_image = tk.Label(self.frm_image)
        self.lbl_image.configure(background=self.background_color)
        self.lbl_image.grid(row=0, column=0, sticky="nsew")

    def create_image_container(self):
        self.lbl_image = tk.Label(self.frm_image)
        self.lbl_image.configure(background=self.background_color)
        self.lbl_image.grid(row=0, column=0, sticky="nsew")

    def show_image(self):
        """Opens the file manager to ask for a image then shows it."""
        global img
        global filepath
        filepath = askopenfilename(
            filetypes=[("Image Files", "*.png"), ("All Files", "*.*")]
        )
        img = Image.open(filepath)
        img = ImageTk.PhotoImage(img)
        self.lbl_image.configure(background="red")
        self.lbl_image.config(image=img)

    def show_resized_image(self):
        """Shows the resized image"""
        global resized_img
        try:
            raw_img = Image.open(filepath)
            height = int(self.ent_height.get())
            width = int(self.ent_width.get())
            resized_img = raw_img.resize((width, height))
            resized_img = ImageTk.PhotoImage(resized_img)
            self.lbl_image.config(image=resized_img)
        except NameError:
            showerror("NO IMAGE", "No image selected!")
        except ValueError:
            showerror("INVALID DIMENSIONS", "Please Provide a Valid Height and Width")
        except AttributeError:
            showerror("NO IMAGE", "No image selected!")

    def save_resized_image(self):
        """Saves the resized image"""
        try:
            pil_image = Image.open(filepath)
            height = int(self.ent_height.get())
            width = int(self.ent_width.get())
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


if __name__ == "__main__":
    app1 = ImageResizer()
    app1.create_frames()
    app1.create_input_tools()
    app1.create_buttons()
    app1.create_image_container()
    app1.window.mainloop()
