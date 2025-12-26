class Payroll:

    STANDARD_DAYS = 25
    GRACE_DAYS = 23

    def calculate_salary(self, employee, attendance_days):

        # FULL TIME EMPLOYEE 
        if hasattr(employee, "monthly_salary"):
            monthly_salary = employee.monthly_salary
            per_day_salary = monthly_salary / self.STANDARD_DAYS

            # Deduction if attendance < grace days
            if attendance_days < self.GRACE_DAYS:
                deduction_days = self.STANDARD_DAYS - attendance_days
                deduction = deduction_days * per_day_salary
            else:
                deduction = 0

            # Double pay after 25 days
            if attendance_days > self.STANDARD_DAYS:
                extra_days = attendance_days - self.STANDARD_DAYS
                bonus = extra_days * per_day_salary * 2
            else:
                bonus = 0

            tax = monthly_salary * 0.15
            net_salary = monthly_salary - deduction + bonus - tax

        #  CONTRACT EMPLOYEE 
        else:
            per_day_salary = employee.per_day_salary

            # Base salary up to 25 days
            payable_days = min(attendance_days, self.STANDARD_DAYS)
            salary = payable_days * per_day_salary

            # Double pay after 25 days
            if attendance_days > self.STANDARD_DAYS:
                extra_days = attendance_days - self.STANDARD_DAYS
                bonus = extra_days * per_day_salary * 2
            else:
                bonus = 0

            tax = salary * 0.10
            net_salary = salary + bonus - tax

        return round(net_salary, 2)
