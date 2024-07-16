import tkinter as tk
from tkinter import messagebox


class InvalidTaskInput(Exception):
    """Custom exception for invalid task input."""
    pass


class GUI:
    def __init__(self, root):
        self.counter = 1
        self.task_array = []
        self.done_array = []
        self.task_widgets = {}
        self.root = root
        self.root.title("GUI")

        # Create an entry widget
        self.entry = tk.Entry(self.root)
        self.entry.pack(fill=tk.X, expand=True)

        # Create a button
        self.button = tk.Button(self.root, text="Add Task", command=self.on_button_click)
        self.button.pack(fill=tk.BOTH)

        # Create a label to show the number of tasks added
        self.label = tk.Label(self.root, text="")
        self.label.pack()

        # Frame to hold tasks
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(side=tk.LEFT, expand=True)

        # Frame to hold completed tasks
        self.done_frame = tk.Frame(self.root)
        self.done_frame.pack(side=tk.RIGHT, expand=True)

    def on_button_click(self):
        user_input = self.entry.get()
        try:
            self.validate_input(user_input)
            task = f"{self.counter}) {user_input}"
            self.task_array.append(task)
            self.add_task_widget(task, self.task_frame, False)
            self.label.config(text=f"Tasks Added: {self.counter}")
            self.counter += 1
            self.entry.delete(0, tk.END)  # Clear the entry widget after adding the task
        except InvalidTaskInput as e:
            messagebox.showerror("Invalid Input", str(e))
        self.entry.delete(0, tk.END)

    def add_task_widget(self, task, frame, done):
        task_var = tk.BooleanVar(value=done)
        checkbox = tk.Checkbutton(frame, variable=task_var)
        label = tk.Label(frame, text=task)

        if done:
            label.config(fg="grey", text=task + " (Done)")
        checkbox.pack(side="left")
        label.pack(side="left")

        task_frame = tk.Frame(frame)
        task_frame.pack(fill="x")

        checkbox.config(command=lambda: self.update_task_status(task_var, task, task_frame))

        self.task_widgets[task] = (task_var, checkbox, label, task_frame)

    def update_task_status(self, var, task, task_frame):
        if var.get():
            self.task_array.remove(task)
            self.done_array.append(task)
        else:
            self.done_array.remove(task)
            self.task_array.append(task)

        # Destroy the old task frame
        task_frame.destroy()

        # Recreate the task widget in the appropriate frame
        if var.get():
            self.add_task_widget(task, self.done_frame, True)
        else:
            self.add_task_widget(task, self.task_frame, False)

    @staticmethod
    def validate_input(user_input):
        if not user_input:  # or user_input != " " or user_input != "  "
            raise InvalidTaskInput("Task cannot be empty or only spaces!")


if __name__ == "__main__":
    tk_root = tk.Tk()
    gui = GUI(tk_root)
    tk_root.mainloop()
