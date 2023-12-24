'''WAP to display grade of students base on marks entered.
70>=distinction
60>=first class
50>=second class
otherwize pass class'''
marks=int(input("Enter the marks: "))
if marks>=70:
    print("distinction")
elif marks>=60:
    print("first class")
elif marks>=50:
    print("second class")
else:
    print("pass")
