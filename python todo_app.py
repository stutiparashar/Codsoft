import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, description, start_time, end_time, priority):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.name} - {self.description} ({self.start_time} - {self.end_time}) Priority: {self.priority}"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg='#1a1a1a')

        header_frame = tk.Frame(self.root, bg='#1a1a1a')
        header_frame.pack(fill=tk.X)

        tk.Label(header_frame, text="To-Do List", bg='#1a1a1a', fg='#ffffff', font=('Helvetica', 18)).pack(pady=10)

        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.pack(fill=tk.BOTH, expand=True)

        task_list_frame = tk.Frame(main_frame, bg='#1a1a1a')
        task_list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.task_listbox = tk.Listbox(task_list_frame, width=40, height=20, bg='#333333', fg='#ffffff', selectbackground='#555555')
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(task_list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        detail_frame = tk.Frame(main_frame, bg='#1a1a1a')
        detail_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.create_entry(detail_frame, "Task Name:", "task_name_entry")
        self.create_entry(detail_frame, "Description:", "task_desc_entry")
        self.create_entry(detail_frame, "Start Time:", "task_start_time_entry")
        self.create_entry(detail_frame, "End Time:", "task_end_time_entry")
        self.create_priority_radiobuttons(detail_frame)
        self.create_buttons(detail_frame)

        self.task_listbox.bind("<<ListboxSelect>>", self.show_task_details)

    def create_entry(self, frame, text, attr):
        tk.Label(frame, text=text, bg='#1a1a1a', fg='#ffffff').pack(anchor=tk.W)
        setattr(self, attr, tk.Entry(frame, bg='#333333', fg='#ffffff', insertbackground='#ffffff'))
        getattr(self, attr).pack(fill=tk.X)

    def create_priority_radiobuttons(self, frame):
        tk.Label(frame, text="Priority:", bg='#1a1a1a', fg='#ffffff').pack(anchor=tk.W)
        self.priority_var = tk.StringVar(value='Medium')
        priority_frame = tk.Frame(frame, bg='#1a1a1a')
        priority_frame.pack(fill=tk.X)
        for text, value in [("High", "High"), ("Medium", "Medium"), ("Low", "Low")]:
            tk.Radiobutton(priority_frame, text=text, variable=self.priority_var, value=value, bg='#1a1a1a', fg='#ffffff', selectcolor='#555555').pack(side=tk.LEFT, fill=tk.X, expand=True)

    def create_buttons(self, frame):
        button_frame = tk.Frame(frame, bg='#1a1a1a')
        button_frame.pack(fill=tk.X, pady=10)
        for text, command in [("Create Task", self.add_task), ("Edit Task", self.edit_task), ("Delete Task", self.delete_task)]:
            tk.Button(button_frame, text=text, command=command, bg='#6666ff', fg='#ffffff').pack(side=tk.LEFT, fill=tk.X, expand=True)

    def add_task(self):
        self.modify_task(add=True)

    def edit_task(self):
        self.modify_task(add=False)

    def modify_task(self, add):
        name = self.task_name_entry.get()
        description = self.task_desc_entry.get()
        start_time = self.task_start_time_entry.get()
        end_time = self.task_end_time_entry.get()
        priority = self.priority_var.get()
        if not all([name, description, start_time, end_time]):
            messagebox.showwarning("Warning", "Please fill in all fields")
            return
        if add:
            self.tasks.append(Task(name, description, start_time, end_time, priority))
        else:
            selected_index = self.task_listbox.curselection()
            if selected_index:
                selected_task = self.tasks[selected_index[0]]
                selected_task.name = name
                selected_task.description = description
                selected_task.start_time = start_time
                selected_task.end_time = end_time
                selected_task.priority = priority
            else:
                messagebox.showwarning("Warning", "Select a task to edit")
                return
        self.update_task_listbox()
        self.clear_entries()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Select a task to delete")

    def show_task_details(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]
            self.task_name_entry.delete(0, tk.END)
            self.task_name_entry.insert(0, selected_task.name)
            self.task_desc_entry.delete(0, tk.END)
            self.task_desc_entry.insert(0, selected_task.description)
            self.task_start_time_entry.delete(0, tk.END)
            self.task_start_time_entry.insert(0, selected_task.start_time)
            self.task_end_time_entry.delete(0, tk.END)
            self.task_end_time_entry.insert(0, selected_task.end_time)
            self.priority_var.set(selected_task.priority)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))

    def clear_entries(self):
        self.task_name_entry.delete(0, tk.END)
        self.task_desc_entry.delete(0, tk.END)
        self.task_start_time_entry.delete(0, tk.END)
        self.task_end_time_entry.delete(0, tk.END)
        self.priority_var.set('Medium')

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
