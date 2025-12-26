class Attendance:
    def __init__(self):
        self.records = {}  # emp_id : days_present

    def mark_attendance(self, emp_id, days_present):
        self.records[emp_id] = days_present

    def get_attendance(self, emp_id):
        return self.records.get(emp_id, 0)
