import tkinter

def add(*args):
    res = 0
    for a in args:
        res += a
    return res


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(add(2, 4, 6, 7, 8))
print(calculate(2, add=5, multiply=4))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="nissan", model="GT-R")
print(f"My car is {my_car.make}, model: {my_car.model}")





def spinbox_used():
    print(spinbox.get())


def scale_used(value):
    print(value)


def checkbutton_used():
    print(checked_state.get())


def radio_used():
    print(radio_state.get())


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


spinbox = tkinter.Spinbox(from_=0, to=100, command=spinbox_used)

scale = tkinter.Scale(from_=0, to=100, command=scale_used)

checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

text = tkinter.Text(height=5, width=30)
text.focus()
text.insert("Example of multi-line text entry.", END)
print(text.get("1.0", END))
text.pack()


