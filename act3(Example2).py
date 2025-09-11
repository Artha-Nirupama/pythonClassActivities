import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ---------------------------
# Database Connection
# ---------------------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",     # Change if needed
        user="root",          # Your MySQL username
        password="artha20@",  # Your MySQL password
        database="studentdb"
    )

# ---------------------------
# Functions for Button Actions
# ---------------------------
def insert_record():
    if not (entry_id.get() and entry_name.get() and entry_address.get() and entry_phone.get() and entry_grade.get()):
        messagebox.showwarning("Input Error", "Please fill all fields")
        return
    
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (student_id, name, address, phone, grade) VALUES (%s, %s, %s, %s, %s)",
                       (entry_id.get(), entry_name.get(), entry_address.get(), entry_phone.get(), entry_grade.get()))
        conn.commit()
        load_records()
        reset_fields()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))
    finally:
        cursor.close()
        conn.close()

def update_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a record to update")
        return
    
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE students SET name=%s, address=%s, phone=%s, grade=%s WHERE student_id=%s",
                       (entry_name.get(), entry_address.get(), entry_phone.get(), entry_grade.get(), entry_id.get()))
        conn.commit()
        load_records()
        reset_fields()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))
    finally:
        cursor.close()
        conn.close()

def delete_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a record to delete")
        return

    student_id = tree.item(selected)["values"][0]

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE student_id=%s", (student_id,))
        conn.commit()
        load_records()
        reset_fields()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))
    finally:
        cursor.close()
        conn.close()

def search_record():
    query = entry_name.get().lower()
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students WHERE LOWER(name) LIKE %s", ("%" + query + "%",))
        rows = cursor.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
    finally:
        cursor.close()
        conn.close()

def reset_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_grade.delete(0, tk.END)

def select_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a record to load")
        return
    values = tree.item(selected)["values"]
    reset_fields()
    entry_id.insert(0, values[0])
    entry_name.insert(0, values[1])
    entry_address.insert(0, values[2])
    entry_phone.insert(0, values[3])
    entry_grade.insert(0, values[4])

def load_records():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("", "end", values=row)
    cursor.close()
    conn.close()

# ---------------------------
# Main Window
# ---------------------------
root = tk.Tk()
root.title("Student Registration System with MySQL")
root.geometry("750x550")
root.configure(bg="white")

# ---------------------------
# Input Fields
# ---------------------------
tk.Label(root, text="Student ID", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Student Name", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Address", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_address = tk.Entry(root)
entry_address.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Phone No", bg="white").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_phone = tk.Entry(root)
entry_phone.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Grade", bg="white").grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_grade = tk.Entry(root)
entry_grade.grid(row=4, column=1, padx=10, pady=5)

# ---------------------------
# Buttons
# ---------------------------
btn_insert = tk.Button(root, text="Insert", bg="red", fg="white", width=10, command=insert_record)
btn_insert.grid(row=0, column=2, padx=10, pady=5)

btn_update = tk.Button(root, text="Update", bg="cyan", width=10, command=update_record)
btn_update.grid(row=1, column=2, padx=10, pady=5)

btn_delete = tk.Button(root, text="Delete", bg="yellow", width=10, command=delete_record)
btn_delete.grid(row=2, column=2, padx=10, pady=5)

btn_search = tk.Button(root, text="Search", bg="blue", fg="white", width=10, command=search_record)
btn_search.grid(row=3, column=2, padx=10, pady=5)

btn_reset = tk.Button(root, text="Reset", bg="orange", width=10, command=reset_fields)
btn_reset.grid(row=4, column=2, padx=10, pady=5)

btn_select = tk.Button(root, text="Select", bg="purple", fg="white", width=10, command=select_record)
btn_select.grid(row=5, column=2, padx=10, pady=5)

# ---------------------------
# Table
# ---------------------------
columns = ("Student ID", "Student Name", "Address", "Phone No", "Grade")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# Load data when app starts
load_records()

# ---------------------------
# Run the App
# ---------------------------
root.mainloop()
