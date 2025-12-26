class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display_details(self):
        print("Employee ID   :", self.emp_id)
        print("Employee Name :", self.name)


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary


class ContractEmployee(Employee):
    def __init__(self, emp_id, name, per_day_salary):
        super().__init__(emp_id, name)
        self.per_day_salary = per_day_salary
