import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Changeme1234",
            database="employee_db"
        )
        return conn  
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error connecting to MySQL: {err}")
        return None 
    
def edit_employee():   
    empid = empid_entry.get()
    name = name_entry.get()
    position = position_entry.get()
    department = department_entry.get()
    salary = salary_entry.get()

    conn = connect_to_mysql()
    cursor = conn.cursor()

    try:
        sql = "UPDATE employees1 SET name=%s, position=%s, department=%s, salary=%s WHERE empid=%s"
        cursor.execute(sql, (name, position, department, salary, empid))
        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Employee edited Successfully")
        else:
            messagebox.showinfo("No Change", "No changes made to employee")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error updating employee: {err}")
    finally:
        cursor.close()
        conn.close()

    empid_entry.delete("0", "end")
    name_entry.delete("0", "end")
    salary_entry.delete("0", "end")

        
def del_employee():
    empid = empid_entry.get()
    conn = connect_to_mysql()

    if conn:
        cursor = conn.cursor()

        try:
            sql = "DELETE FROM employees1 WHERE empid=%s"
            cursor.execute(sql, (empid,))
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Employee(s) Deleted Successfully")
            else:
                messagebox.showinfo("No Change", "No employee found with given ID")

            empid_entry.delete("0", "end")
            name_entry.delete("0", "end")
            salary_entry.delete("0", "end")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error deleting employee: {err}")
        finally:
            cursor.close()
            conn.close()




def add_employee():
    empid=empid_entry.get()
    name = name_entry.get()
    position = position_entry.get()
    department = department_entry.get()
    salary = salary_entry.get()
    conn = connect_to_mysql()
    cursor = conn.cursor()
    if conn:
        try:
            if empid.isnumeric():
                if name.isalpha(): 
                    if position.isalpha():
                        if department.isalpha():
                            if salary.isnumeric():
                                sql = "INSERT INTO employees1 (empid, name, position, department, salary) VALUES (%s, %s, %s, %s, %s)"
                                cursor.execute(sql, (empid, name, position, department, salary))
                                conn.commit()
                                messagebox.showinfo("Success", "Employee added successfully!")
                                fetch_employees() 
                            else:
                                messagebox.showinfo("Error","Salary is invalid") 
                        else:
                            messagebox.showinfo("Error","Domain is invalid")
                    else:
                        messagebox.showinfo("Error","Position is invalid")
                else:
                    messagebox.showinfo("Error","Name is invalid")
            else:
                messagebox.showinfo("Error","Employee ID is invalid")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error adding employee: {err}")
        finally:
            cursor.close()
            conn.close()
            empid_entry.delete("0","end")
            name_entry.delete("0","end")
            salary_entry.delete("0","end")


def fetch_employees():
    conn = connect_to_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees1")
            employees = cursor.fetchall()

            employees_frame = tk.Toplevel()
            employees_frame.title("Employees") 
            display_employees(employees, employees_frame)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error fetching employees: {err}")
        finally:
            cursor.close()
            conn.close()


def display_employees(employees,employees_frame):

    for employee in employees:
        employee_label = tk.Label(employees_frame, text=f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Department: {employee[3]}, Salary: {employee[4]}")
        employee_label.pack()
                  
        
    
def search_employee():
    emp_id = empid_entry.get()
    conn = connect_to_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM employees1 WHERE empid = %s"
            cursor.execute(sql, (emp_id,))
            employee = cursor.fetchone()  
            if employee:
                name_entry.delete("0","end")
                position_entry.set(employee[2])
                department_entry.set(employee[3])
                salary_entry.delete("0","end")
                name_entry.insert(0,employee[1])
                salary_entry.insert(0,employee[4])
                messagebox.showinfo("Employee Found", f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Department: {employee[3]}, Salary: {employee[4]}")
            else:
                messagebox.showinfo("Employee Not Found", f"No employee found with ID: {emp_id}")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error searching for employee: {err}")
        finally:
            cursor.close()
            conn.close()

        
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
  
