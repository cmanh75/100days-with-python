from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    result_label.config(text=f"{round(miles * 1.609)}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)

window.mainloop()
