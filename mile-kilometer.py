from tkinter import *

def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.609, 2)
        kilometer_result_label.config(text=f"{km}")
    except ValueError:
        kilometer_result_label.config(text="Invalid input")

# Create the main window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Input field for miles
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# "is equal to" label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Kilometer result label
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Km label
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Start the event loop
window.mainloop()