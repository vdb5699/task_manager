import tkinter as tk
from tkinter import messagebox


class InvalidTaskInput(Exception):
    """Custom exception for invalid task input."""
    pass


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
        self.task_frame.pack(side="left")

        # Frame to hold completed tasks
        self.done_frame = tk.Frame(self.root)
        self.done_frame.pack(side="right")

    def on_button_click(self):
        user_input = self.entry.get().strip()
        try:
            validate_input(user_input)
            task = f"{self.counter}) {user_input}"
            self.task_array.append(task)
            # self.add_task_widget(task, self.task_frame, False)
            self.label.config(text=f"Tasks Added: {self.counter}")
            self.counter += 1
            self.entry.delete(0, tk.END)  # Clear the entry widget after adding the task
        except InvalidTaskInput as e:
            messagebox.showerror("Invalid Input", str(e))
        self.entry.delete(0, tk.END)

    # def add_task_widget(self, task, frame, done):


def validate_input(user_input):
    if not user_input:  # or user_input != " " or user_input != "  "
        raise InvalidTaskInput("Task cannot be empty or only spaces!")


if __name__ == "__main__":
    tk_root = tk.Tk()
    gui = GUI(tk_root)

    tk_root.mainloop()
