class Student:
    # Class variables to count the number of students for each department
    total_students = 0
    btech_students = 0
    pgdm_students = 0

    def __init__(self, name, department):
        # Instance variables
        self.name = name
        self.department = department

        # Increment the total_students count
        Student.total_students += 1

        # Increment the department-specific count
        if department.upper() == "BTECH":
            Student.btech_students += 1
        elif department.upper() == "PGDM":
            Student.pgdm_students += 1

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}\n")

# Function to admit students
def admit_students():
    # Number of students to admit
    num_students = int(input("Enter the number of students to admit: "))

    # Creating a list to store student objects
    students_list = []

    # Loop to take user inputs for each student
    for i in range(num_students):
        name = input(f"Enter the name of student {i + 1}: ")
        department = input(f"Enter the department for {name} (BTech/PGDM): ")

        # Creating an object of the Student class and adding it to the list
        student = Student(name, department)
        students_list.append(student)

    # Displaying student details
    print("\nStudent Details:")
    for student in students_list:
        student.display_details()

    # Displaying the total number of students
    print(f"\nTotal Students Admitted: {Student.total_students}")
    print(f"BTech Students: {Student.btech_students}")
    print(f"PGDM Students: {Student.pgdm_students}")

# Calling the function to admit students
admit_students()
