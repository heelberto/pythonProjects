import tkinter

def change_label():
    my_label.config(text=f"{entry.get()}")

def print_entry_text():
    entry_text = entry.get()
    print(entry_text)


window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0, padx=15, pady=15)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2,row=0,  padx=15, pady=15)


button = tkinter.Button(text="Click me", command=change_label)
button.grid(column=1, row=1,  padx=15, pady=15)

entry = tkinter.Entry(width=10)
entry.grid(column=3,row=3,  padx=15, pady=15)

print_button = tkinter.Button(text="Print Entry Text", command=change_label)
#print_button.pack(pady=10)












window.mainloop()
