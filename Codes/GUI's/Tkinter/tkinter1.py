# Steps
# 1. Imports and creating a window
import tkinter as tk

window = tk.Tk()
window.title("C to F Converter")
# window.resizable(width=False, height=False)
frame_1 = tk.Frame(window)
frame_2 = tk.Frame(window)

# 2. Label to enter the temperature
ent_temp = tk.Entry(master=frame_1, width=10)
ent_temp.grid(row=0, column=0)

# 3. Button to convert the temperature to Fahrenheit
btn_convert = tk.Button(master=frame_2, text="Convert")
btn_convert.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# 4. Label which shows the comverted temperature
lbl_new_tem = tk.Label(master=frame_1, text="")
lbl_new_tem.grid(row=0, column=1)

# 5. Function for the conversion
def convert(event):
    try:
        celc = ent_temp.get()
        fahr = float(celc) * 1.8 + 32
        lbl_new_tem["text"] = fahr
    except:
        lbl_new_tem["text"] = "Invalid Input"


# 6. Binding the button to the function
btn_convert.bind("<Button-1>", convert)
frame_1.grid(row=0, column=0, sticky="ew")
frame_2.grid(row=1, column=0, sticky="ew")
window.mainloop()
