import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


def button_clicked():
    my_label.config(text=input.get())


my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New text"
my_label.config(text="New text")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="And Me", command=button_clicked)
button2.grid(column=2, row=0)


input = tkinter.Entry(width=10)
input.grid(column=3, row=3)
print(input.get())

window.mainloop()
