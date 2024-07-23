import operator
from tkinter import *
import tkinter as tk


class calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(0, 0)
        self.array = []

        # Create Entry Widget
        self.entry = tk.Entry(self.root)

        # Create Buttons
        self.button_1 = tk.Button(self.root, text="1", padx=40, pady=20, command=lambda: button_click(self, '1'))
        self.button_2 = tk.Button(self.root, text="2", padx=40, pady=20, command=lambda: button_click(self, "2"))
        self.button_3 = tk.Button(self.root, text="3", padx=40, pady=20, command=lambda: button_click(self, "3"))
        self.button_4 = tk.Button(self.root, text="4", padx=40, pady=20, command=lambda: button_click(self, "4"))
        self.button_5 = tk.Button(self.root, text="5", padx=40, pady=20, command=lambda: button_click(self, "5"))
        self.button_6 = tk.Button(self.root, text="6", padx=40, pady=20, command=lambda: button_click(self, "6"))
        self.button_7 = tk.Button(self.root, text="7", padx=40, pady=20, command=lambda: button_click(self, "7"))
        self.button_8 = tk.Button(self.root, text="8", padx=40, pady=20, command=lambda: button_click(self, "8"))
        self.button_9 = tk.Button(self.root, text="9", padx=40, pady=20, command=lambda: button_click(self, "9"))
        self.button_0 = tk.Button(self.root, text="0", padx=40, pady=20, command=lambda: button_click(self, "0"))
        self.button_plus = tk.Button(self.root, text="+", padx=40, pady=20, command=lambda: button_click(self, "+"))
        self.button_minus = tk.Button(self.root, text="-", padx=40, pady=20, command=lambda: button_click(self, "-"))
        self.button_divide = tk.Button(self.root, text="/", padx=40, pady=20, command=lambda: button_click(self, "/"))
        self.button_times = tk.Button(self.root, text="X", padx=40, pady=20, command=lambda: button_click(self, "X"))
        self.button_point = tk.Button(self.root, text=".", padx=40, pady=20, command=lambda: button_click(self, "."))
        self.button_clear = tk.Button(self.root, text="CE", padx=40, pady=20, command=lambda: button_click(self, "CE"))
        self.button_equals = tk.Button(self.root, text="=", padx=40, pady=20, command=lambda: button_click(self, "="),
                                       background="green")
        self.button_backspace = tk.Button(self.root, text="C", padx=40, pady=20,
                                          command=lambda: button_click(self, "C"))

        # Organising widget and buttons based on Grid
        self.button_point.grid(row=4, column=0)
        self.button_0.grid(row=4, column=1)
        self.button_clear.grid(row=4, column=2)
        self.button_equals.grid(row=4, column=3)

        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)
        self.button_plus.grid(row=3, column=3)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.button_minus.grid(row=2, column=3)

        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)
        self.button_times.grid(row=1, column=3)

        self.entry.grid(row=0, column=0, columnspan=2)
        self.button_backspace.grid(row=0, column=2)
        self.button_divide.grid(row=0, column=3)


def button_click(self, text):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,  # use operator.div for Python 2
        "%": operator.mod,
        "^": operator.xor,
    }

    if text == "=":
        value2 = self.entry.get()
        self.array.append(value2)
        value1 = self.array[0]
        operator_value = self.array[1]
        self.entry.delete(0, END)
        answer = ops[operator_value](int(value2), int(value1))
        self.entry.insert(0, answer)
        self.array.append(answer)
    elif text == "+":
        value = self.entry.get()
        self.array.append(value)
        self.array.append("+")
        self.entry.delete(0, END)
    elif text == "-":
        value = self.entry.get()
        self.array.append(value)
        self.array.append("-")
        self.entry.delete(0, END)
    elif text == "/":
        value = self.entry.get()
        self.array.append(value)
        self.array.append("/")
        self.entry.delete(0, END)
    elif text == "X":
        value = self.entry.get()
        self.array.append(value)
        self.array.append("X")
    elif text == "CE":
        self.entry.delete(0, END)
        self.array.clear()
    elif text == "C":
        self.entry.delete(0, 1)
    elif text == "1":
        text = 1
        self.entry.insert(0, text)
        print(text)
    elif text == "2":
        text = 2
        self.entry.insert(0, text)
        print(text)
    elif text == "3":
        text = 3
        self.entry.insert(0, text)
        print(text)
    elif text == "4":
        text = 4
        self.entry.insert(0, text)
        print(text)
    elif text == "5":
        text = 5
        self.entry.insert(0, text)
        print(text)
    elif text == "6":
        text = 6
        self.entry.insert(0, text)
        print(text)
    elif text == "7":
        text = 7
        self.entry.insert(0, text)
        print(text)
    elif text == "8":
        text = 8
        self.entry.insert(0, text)
        print(text)
    elif text == "9":
        text = 9
        self.entry.insert(0, text)
        print(text)
    elif text == "0":
        text = 0
        self.entry.insert(0, text)
        print(text)

    print(self.array)


if __name__ == "__main__":
    tk_root = tk.Tk()
    Calculator = calculator(tk_root)
    tk_root.mainloop()
