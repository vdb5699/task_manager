import tkinter as tk


class GUI:
    # constructor method
    def __init__(self, root):
        self.counter = 1
        self.task_array = []
        self.user_input = None
        self.root = root
        self.root.title("GUI")

        # Create an entry widget
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        # Create a button
        self.button = tk.Button(self.root, text="Add Task", command=self.on_button_click)
        self.button.pack()

        # Create a label
        self.label = tk.Label(self.root, text="")
        self.label.pack()

        # Create a label to show the number of tasks added
        self.label = tk.Label(self.root, text="")
        self.label.pack()

        # Frame to hold tasks
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack()

        # Frame to hold completed tasks
        self.done_frame = tk.Frame(self.root)
        self.done_frame.pack()

    def on_button_click(self):
        self.label.config(text=f"Tasks Added: {self.counter}")
        self.task_label = tk.Label(self.root)
        self.task_label.pack()
        self.checkbox = tk.Checkbutton(self.root)
        self.checkbox.pack()
        self.user_input = self.entry.get()
        self.task_array.append(str(self.counter) + ") " + self.user_input)
        self.task_label.config(text=f"{self.task_array[self.counter - 1]}")
        self.counter += 1


if __name__ == "__main__":
    tk_root = tk.Tk()
    gui = GUI(tk_root)

    tk_root.mainloop()
