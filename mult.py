class LetsUpgrade:
    a = [["Python", "CPP", "Java"], ["Saurabh sir", "Sai sir", "Prasad sir"], ["12:00", "15:00", "02:00"]]

class ITM:
    b = [["Soft skills", "Business Studies", "Entrepreneurship"], ["Sakshi ma'am", "Sheetal ma'am", "Sumit sir"],
         ["16:00", "19:00", "23:00"]]

class Btech(LetsUpgrade, ITM):
    def __init__(self):
        self.subjects = []

    def courses(self):
        print("LetsUpgrade")
        for i in range(3):
            print(i + 1, "=", LetsUpgrade.a[0][i], "--", LetsUpgrade.a[1][i], "--", LetsUpgrade.a[2][i])
        print()
        print("ITM")
        for i in range(3):
            print(i + 4, "=", ITM.b[0][i], "--", ITM.b[1][i], "--", ITM.b[2][i])

    def choice(self):
        num_subjects = int(input("Enter the number of subjects: "))
        for _ in range(num_subjects):
            subject_no = int(input("Enter the subject no.: "))
            self.subjects.append(subject_no)

    def show_invoice(self):
        total_duration = 0
        print("\nInvoice:")
        for subject_no in self.subjects:
            if 1 <= subject_no <= 3:
                category = LetsUpgrade
                subject_index = subject_no - 1
            elif 4 <= subject_no <= 6:
                category = ITM
                subject_index = subject_no - 4
            else:
                print(f"Invalid subject no.: {subject_no}")
                continue

            course_name = category.a[0][subject_index] if hasattr(category, 'a') else category.b[0][subject_index]
            instructor = category.a[1][subject_index] if hasattr(category, 'a') else category.b[1][subject_index]
            duration = category.a[2][subject_index] if hasattr(category, 'a') else category.b[2][subject_index]
            total_duration += int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])

            print(f"Subject {subject_no}: {course_name} - {instructor} - {duration} hours")

        print(f"\nTotal Duration: {total_duration // 60} hours {total_duration % 60} minutes")


# Create an object of the derived class
obj = Btech()

# Access methods from base classes
obj.courses()
obj.choice()
obj.show_invoice()
