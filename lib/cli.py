import sys
import os

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from lib.db.models import session, Department, Employee

# Main Menu
def main_menu():
    while True:
        print("\nCompany Employee Tracker")
        print("1. Manage Departments")
        print("2. Manage Employees")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            department_menu()
        elif choice == "2":
            employee_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Department Management
def department_menu():
    while True:
        print("\nManage Departments")
        print("1. Add Department")
        print("2. View All Departments")
        print("3. Update Department")
        print("4. Delete Department")
        print("5. Return to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            add_department()
        elif choice == "2":
            view_departments()
        elif choice == "3":
            update_department()
        elif choice == "4":
            delete_department()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

def add_department():
    name = input("Enter department name: ")
    location = input("Enter location: ")
    new_department = Department(name=name, location=location)
    session.add(new_department)
    session.commit()
    print("Department added successfully!")

def view_departments():
    departments = session.query(Department).all()
    if departments:
        for dept in departments:
            print(f"ID: {dept.id}, Name: {dept.name}, Location: {dept.location}")
    else:
        print("No departments found.")

def update_department():
    view_departments()
    dept_id = input("Enter the ID of the department to update: ")
    department = session.query(Department).get(dept_id)
    if department:
        department.name = input(f"Enter new name (current: {department.name}): ") or department.name
        department.location = input(f"Enter new location (current: {department.location}): ") or department.location
        session.commit()
        print("Department updated successfully!")
    else:
        print("Department not found.")

def delete_department():
    view_departments()
    dept_id = input("Enter the ID of the department to delete: ")
    department = session.query(Department).get(dept_id)
    if department:
        session.delete(department)
        session.commit()
        print("Department deleted successfully!")
    else:
        print("Department not found.")

# Employee Management
def employee_menu():
    while True:
        print("\nManage Employees")
        print("1. Hire Employee")
        print("2. Update Employee")
        print("3. Remove Employee")
        print("4. View Employees by Department")
        print("5. List All Employees")
        print("6. Return to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            hire_employee()
        elif choice == "2":
            update_employee()
        elif choice == "3":
            remove_employee()
        elif choice == "4":
            view_employees_by_department()
        elif choice == "5":
            list_all_employees()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

def hire_employee():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    position = input("Enter position: ")
    salary = input("Enter salary: ")

    view_departments()
    dept_id = input("Enter the department ID for this employee: ")
    department = session.query(Department).get(dept_id)
    if department:
        new_employee = Employee(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            position=position,
            salary=salary,
            department=department,
        )
        session.add(new_employee)
        session.commit()
        print("Employee hired successfully!")
    else:
        print("Invalid department ID.")

def update_employee():
    list_all_employees()
    emp_id = input("Enter the ID of the employee to update: ")
    employee = session.query(Employee).get(emp_id)
    if employee:
        employee.first_name = input(f"New first name ({employee.first_name}): ") or employee.first_name
        employee.last_name = input(f"New last name ({employee.last_name}): ") or employee.last_name
        employee.email = input(f"New email ({employee.email}): ") or employee.email
        employee.phone = input(f"New phone ({employee.phone}): ") or employee.phone
        employee.position = input(f"New position ({employee.position}): ") or employee.position
        employee.salary = input(f"New salary ({employee.salary}): ") or employee.salary
        session.commit()
        print("Employee updated successfully!")
    else:
        print("Employee not found.")

def remove_employee():
    list_all_employees()
    emp_id = input("Enter the ID of the employee to remove: ")
    employee = session.query(Employee).get(emp_id)
    if employee:
        session.delete(employee)
        session.commit()
        print("Employee removed successfully!")
    else:
        print("Employee not found.")

def view_employees_by_department():
    view_departments()
    dept_id = input("Enter the department ID: ")
    department = session.query(Department).get(dept_id)
    if department and department.employees:
        for emp in department.employees:
            print(f"ID: {emp.id}, Name: {emp.first_name} {emp.last_name}, Position: {emp.position}")
    else:
        print("No employees found for this department.")

def list_all_employees():
    employees = session.query(Employee).all()
    if employees:
        for emp in employees:
            print(
                f"ID: {emp.id}, Name: {emp.first_name} {emp.last_name}, Position: {emp.position}, Department: {emp.department.name}"
            )
    else:
        print("No employees found.")

if __name__ == "__main__":
    main_menu()
