

import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("To-Do List")

# Task list storage
tasks = []

# Function to update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete a task
def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to mark a task as complete
def complete_task():
    selected_task = listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        tasks[task_index] = f"✔ {tasks[task_index]}"  # Mark with a check
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to mark complete!")

# UI Layout
frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack()

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=2)

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(pady=2)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=2)

# Run the application
root.mainloop()