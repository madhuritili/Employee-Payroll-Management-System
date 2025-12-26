# Employee Payroll Management System

## 📌 Project Overview
A console-driven employee payroll management system developed using Python and object-oriented programming to calculate salaries based on attendance, employee type, tax deductions, and overtime bonuses.  
The application supports persistent data storage and generates payslips for employees.

---

## 🚀 Features
- Add Full-Time and Contract Employees
- Attendance tracking for each employee
- Attendance-based salary calculation
- Tax deduction handling
- Overtime bonus calculation
- Payslip generation and storage
- File-based data persistence
- Menu-driven console interface
- Object-Oriented Programming design

---

## 🛠️ Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- File Handling

---

## ▶️ How to Run the Project

1. **Clone the repository**
git clone https://github.com/your-username/employee-payroll-system.git

2. **Navigate to the project directory**
cd employee-payroll-system

3. **Run the application**
python main.py


📂 Project Structure
markdown
Copy code
employee-payroll-system/
├── main.py
├── payroll/
│   ├── __init__.py
│   ├── employee.py
│   └── payroll.py
├── attendance/
│   ├── __init__.py
│   └── attendance.py
├── employees.txt
├── attendance.txt
├── payslips.txt
└── README.md
📄 Data Files
employees.txt – Stores employee details

attendance.txt – Stores attendance records

payslips.txt – Stores generated payslips

📊 Salary Calculation Logic
Full-Time Employees
Fixed monthly salary

Standard working days: 25

Grace days: 23

Tax deduction: 15%

Overtime bonus: Double pay for days worked beyond 25

Contract Employees
Paid on a per-day basis

Salary calculated up to 25 working days

Overtime bonus: Double pay for days worked beyond 25

Tax deduction: 10%

🎯 Learning Outcomes
Implementation of Object-Oriented Programming concepts

Practical usage of file handling in Python

Real-world payroll system logic

Modular and maintainable code design
