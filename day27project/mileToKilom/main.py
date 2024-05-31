import tkinter


def calculate_and_display():
    miles = float(miles_entry.get())
    kilometers = round(miles_to_kilo(miles))
    kilometers_label.config(text=f"{kilometers:.2f}")


def miles_to_kilo(miles):
    return miles * 1.60934


window = tkinter.Tk()
window.title("Miles to Kilometers")


label_spacer = tkinter.Label(text="")
label_spacer.grid(column=0, row=0)

miles_entry = tkinter.Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equalTo_label = tkinter.Label(text="is equal to")
equalTo_label.grid(column=0, row=1)

kilometers_label = tkinter.Label(text="0.0")
kilometers_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = tkinter.Button(text="Calculate", command=calculate_and_display)
calc_button.grid(column=1, row=3)

window.mainloop()
