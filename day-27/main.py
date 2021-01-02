from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Labels
miles_lb = Label(text="Miles")
is_eq_lb = Label(text="is equal to")
km_val_lb = Label(text="0")
km_lb = Label(text="Km")

# Entry
miles_en = Entry()
miles_en.config(width=7)
miles_en.focus()

def convert():
    km = float(miles_en.get()) * 1.60934
    km_val_lb.config(text=f"{km}")


# Button
button = Button(text="Calculate", command=convert)

miles_en.grid(row=0, column=1)
miles_lb.grid(row=0, column=2)

is_eq_lb.grid(row=1, column=0)
km_val_lb.grid(row=1, column=1)
km_lb.grid(row=1, column=2)

button.grid(row=2, column=1)


window.mainloop()
