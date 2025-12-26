# main.py - Simple Employee Payroll System

from payroll.employee import FullTimeEmployee, ContractEmployee
from payroll.payroll import Payroll
from attendance.attendance import Attendance

EMP_FILE = "employees.txt"
ATT_FILE = "attendance.txt"
PAYSLIP_FILE = "payslips.txt"

# ----------- LOAD / SAVE EMPLOYEES -----------
def load_employees():
    employees = {}
    try:
        with open(EMP_FILE, "r", encoding="utf-8") as file:
            for line in file:
                emp_id, emp_type, name, salary = line.strip().split(",")
                if emp_type == "FullTime":
                    employees[int(emp_id)] = FullTimeEmployee(
                        int(emp_id), name, float(salary))
                else:
                    employees[int(emp_id)] = ContractEmployee(int(emp_id), name, float(salary))
    except FileNotFoundError:

        pass
    return employees

def save_employee(emp):
    with open(EMP_FILE, "a", encoding="utf-8") as file:
        if hasattr(emp, "monthly_salary"):
            file.write(f"{emp.emp_id},FullTime,{emp.name},{emp.monthly_salary}\n")
        else:
            file.write(f"{emp.emp_id},Contract,{emp.name},{emp.per_day_salary}\n")

# ----------- LOAD / SAVE ATTENDANCE -----------
def load_attendance(attendance):
    try:
        with open(ATT_FILE, "r") as file:
            for line in file:
                emp_id, days = line.strip().split(",")
                attendance.records[int(emp_id)] = int(days)
    except FileNotFoundError:
        pass

def save_attendance(emp_id, days):
    data = {}
    try:
        with open(ATT_FILE, "r") as file:
            for line in file:
                eid, d = line.strip().split(",")
                data[int(eid)] = int(d)
    except FileNotFoundError:
        pass
    data[emp_id] = days
    with open(ATT_FILE, "w") as file:
        for eid, d in data.items():
            file.write(f"{eid},{d}\n")

# ----------- SAVE PAYSLIP -----------
def save_payslip(emp, days, salary):
    with open(PAYSLIP_FILE, "a") as file:
        file.write("\n----- PAYSLIP -----\n")
        file.write(f"Employee ID   : {emp.emp_id}\n")
        file.write(f"Employee Name : {emp.name}\n")
        if hasattr(emp, "monthly_salary"):
            file.write(f"Employee Type : Full-Time\n")
            file.write(f"Monthly Salary: {emp.monthly_salary}\n")
        else:
            file.write(f"Employee Type : Contract\n")
            file.write(f"Per-Day Salary: {emp.per_day_salary}\n")
        file.write(f"Attendance    : {days} days\n")
        file.write(f"Net Salary    : {salary}\n")
        file.write("-------------------\n")

# ----------- VIEW FUNCTIONS -----------
def view_employee(emp, days, salary):
    print("\n--- EMPLOYEE DETAILS ---")
    print("ID      :", emp.emp_id)
    print("Name    :", emp.name)
    if hasattr(emp, "monthly_salary"):
        print("Type    : Full-Time")
        print("Salary  :", emp.monthly_salary)
    else:
        print("Type    : Contract")
        print("Salary  :", emp.per_day_salary)
    print("Attendance:", days)
    print("Net Salary :", salary)
    print("------------------------")

def view_all_employees(employees, attendance, payroll):
    for emp in employees.values():
        days = attendance.get_attendance(emp.emp_id)
        salary = payroll.calculate_salary(emp, days)
        view_employee(emp, days, salary)

# ----------- MAIN PROGRAM -----------
employees = load_employees()
attendance = Attendance()
load_attendance(attendance)
payroll = Payroll()

while True:
    print("\n===== Employee Payroll =====")
    print("1. Add Full-Time Employee")
    print("2. Add Contract Employee")
    print("3. Mark Attendance")
    print("4. Generate Payslip")
    print("5. View Particular Employee")
    print("6. View All Employees")
    print("7. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            emp_id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            salary = float(input("Enter Monthly Salary: "))
            emp = FullTimeEmployee(emp_id, name, salary)
            employees[emp_id] = emp
            save_employee(emp)
            print("Full-Time Employee Added")

        elif choice == "2":
            emp_id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            per_day_salary = float(input("Enter Per-Day Salary: "))
            emp = ContractEmployee(emp_id, name, per_day_salary)
            employees[emp_id] = emp
            save_employee(emp)
            print("Contract Employee Added")

        elif choice == "3":
            emp_id = int(input("Enter Employee ID: "))
            if emp_id not in employees:
                print("Employee not found")
                continue
            days = int(input("Enter Attendance (0-30): "))
            attendance.mark_attendance(emp_id, days)
            save_attendance(emp_id, days)
            print("Attendance Recorded")

        elif choice == "4":
            emp_id = int(input("Enter Employee ID: "))
            if emp_id not in employees:
                print("Employee not found")
                continue
            emp = employees[emp_id]
            days = attendance.get_attendance(emp_id)
            salary = payroll.calculate_salary(emp, days)
            view_employee(emp, days, salary)
            save_payslip(emp, days, salary)

        elif choice == "5":
            emp_id = int(input("Enter Employee ID: "))
            if emp_id not in employees:
                print("Employee not found")
                continue
            emp = employees[emp_id]
            days = attendance.get_attendance(emp_id)
            salary = payroll.calculate_salary(emp, days)
            view_employee(emp, days, salary)

        elif choice == "6":
            view_all_employees(employees, attendance, payroll)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)
