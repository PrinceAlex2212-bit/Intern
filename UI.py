import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("480x410")
root.title("Employee Management System")


tk.Label(root, text="\nEMPLOYEE DBMS\n\n").pack()

tk.Label(root, text="Empid:").place(x=100,y=50)
empid_entry=tk.Entry(root)
empid_entry.place(x=160, y=50)

tk.Label(root, text="Name:").place(x=100, y=100)
name_entry = tk.Entry(root)
name_entry.place(x=160, y=100)


def on_selection_change(value):
    print(f"Selected: {value}")

tk.Label(root, text="Position:").place(x=100, y=150)
options = ["Intern","HR","TL"]
position_entry=tk.StringVar(root)
position_entry.set(options[0])
dropdown=tk.OptionMenu(root,position_entry,*options,command=on_selection_change)
dropdown.place(x=160,y=150,width=190)

tk.Label(root, text="Domain:").place(x=100, y=200)
options1=["AI","ML","WEB","HR"]
department_entry=tk.StringVar(root)
department_entry.set(options1[0])
dropdown1=tk.OptionMenu(root,department_entry,*options1,command=on_selection_change)
dropdown1.place(x=160,y=200,width=190)

tk.Label(root, text="Salary:").place(x=100, y=250)
salary_entry = tk.Entry(root)
salary_entry.place(x=160, y=250)

add_button = tk.Button(root, text="Add", command=add_employee, width=3)
add_button.place(x=160, y=290)

edit_button = tk.Button(root, text="Edit", command=edit_employee, width=3)
edit_button.place(x=225, y=290)

delete_button = tk.Button(root, text="Delete", command=del_employee, width=3)
delete_button.place(x=290, y=290)

search_button= tk.Button(root, text="Search", command=search_employee,width=3)
search_button.place(x=225,y=330)

fetch_button = tk.Button(root, text="Fetch Employees", command=fetch_employees)
fetch_button.place(x=185, y=370)

root.mainloop()
