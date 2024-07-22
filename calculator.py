import math
import tkinter as tk


class calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(0, 0)

        # Create Entry Widget
        self.entry = tk.Entry(self.root, width=20)

        # Create Buttons
        self.button_1 = tk.Button(self.root, text="1", padx=40, pady=20, command=lambda:button_click('1'))
        self.button_2 = tk.Button(self.root, text="2", padx=40, pady=20, command=lambda:button_click("2"))
        self.button_3 = tk.Button(self.root, text="3", padx=40, pady=20, command=lambda:button_click("3"))
        self.button_4 = tk.Button(self.root, text="4", padx=40, pady=20, command=lambda:button_click("4"))
        self.button_5 = tk.Button(self.root, text="5", padx=40, pady=20, command=lambda:button_click("5"))
        self.button_6 = tk.Button(self.root, text="6", padx=40, pady=20, command=lambda:button_click("6"))
        self.button_7 = tk.Button(self.root, text="7", padx=40, pady=20, command=lambda:button_click("7"))
        self.button_8 = tk.Button(self.root, text="8", padx=40, pady=20, command=lambda:button_click("8"))
        self.button_9 = tk.Button(self.root, text="9", padx=40, pady=20, command=lambda:button_click("9"))
        self.button_0 = tk.Button(self.root, text="0", padx=40, pady=20, command=lambda:button_click("0"))
        self.button_plus = tk.Button(self.root, text="+", padx=40, pady=20, command=lambda:button_click("+"))
        self.button_minus = tk.Button(self.root, text="-", padx=40, pady=20, command=lambda:button_click("-"))
        self.button_divide = tk.Button(self.root, text="/", padx=40, pady=20, command=lambda:button_click("/"))
        self.button_times = tk.Button(self.root, text="X", padx=40, pady=20, command=lambda:button_click("X"))
        self.button_point = tk.Button(self.root, text=".", padx=40, pady=20, command=lambda:button_click("."))
        self.button_clear = tk.Button(self.root, text="CE", padx=40, pady=20, command=lambda:button_click("CE"))
        self.button_equals = tk.Button(self.root, text="=", padx=40, pady=20, command=lambda:button_click("="), background="green")
        self.button_backspace = tk.Button(self.root, text="C", padx=40, pady=20, command=lambda:button_click("C"))

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

        self.entry.grid(row=0, column=1)
        self.button_backspace.grid(row=0, column=2)
        self.button_divide.grid(row=0, column=3)


def button_click(text):
    # if isinstance(text, int):
    #
    # self.text = text
    match text:
        case "1":
            return 1


    print(text)

    return


if __name__ == "__main__":
    tk_root = tk.Tk()
    Calculator = calculator(tk_root)
    tk_root.mainloop()


