import sqlite3
import tkinter as tk
from tkinter import messagebox

# Create Database
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )
""")
conn.commit()
conn.close()

# Function to Add Student
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    if name and age and grade:
        conn = sqlite3.connect("student_db.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student added successfully!")
        show_students()
    else:
        messagebox.showerror("Error", "All fields are required!")

# Function to View Students
def show_students():
    conn = sqlite3.connect("student_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    student_list.delete(0, tk.END)
    for row in rows:
        student_list.insert(tk.END, row)

# Function to Delete Student
def delete_student():
    selected_item = student_list.curselection()
    if selected_item:
        student_id = student_list.get(selected_item)[0]
        conn = sqlite3.connect("student_db.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student deleted successfully!")
        show_students()
    else:
        messagebox.showerror("Error", "Please select a student to delete.")

# GUI Setup
app = tk.Tk()
app.title("Student Management System")
app.geometry("400x400")

tk.Label(app, text="Name").pack()
name_entry = tk.Entry(app)
name_entry.pack()

tk.Label(app, text="Age").pack()
age_entry = tk.Entry(app)
age_entry.pack()

tk.Label(app, text="Grade").pack()
grade_entry = tk.Entry(app)
grade_entry.pack()

tk.Button(app, text="Add Student", command=add_student).pack()
tk.Button(app, text="Delete Student", command=delete_student).pack()
tk.Button(app, text="View Students", command=show_students).pack()

student_list = tk.Listbox(app)
student_list.pack()

app.mainloop()