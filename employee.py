class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def get_employee_details(self):
        """
        Method to get employee details.

        Returns:
        - Tuple containing employee ID, employee name, and employee salary.
        """
        return self.emp_id, self.emp_name, self.emp_salary

    def print_employee_details(self):
        """Method to print employee details."""
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)

# Example usage with user input:
# Taking inputs from the user
emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")
emp_salary = input("Enter Employee Salary: ")

# Creating an Employee object with user inputs
employee1 = Employee(emp_id=emp_id, emp_name=emp_name, emp_salary=emp_salary)

# Getting and printing employee details
details_tuple = employee1.get_employee_details()
print("\nEmployee Details (as tuple):", details_tuple)

print("\nEmployee Details (printed):")
employee1.print_employee_details()