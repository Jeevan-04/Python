'''class Student:
    def __init__(self):
        self.name='ABC'
        self.age=19
    def display(self):
        print("Name:",self.name,"Age:",self.age)
obj=Student()
obj.display()
obj2=Student()
obj2.display()'''

'''class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name,"Age:",self.age)
obj=Student("ABC",180)
obj.display()
obj2=Student("AGE",120)
obj2.display()'''

'''class Student:
    count = 0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.count+=1
    def display(self):
        print("Name:",self.name,"Age:",self.age)
obj=Student("ABC",180)
obj.display()
obj2=Student("AGE",120)
obj2.display()
print(Student.count)'''

'''class Student:
    count = 0
    def get(self,i):
        for n in range(i):
            self.name=input("Enter your Name: ")
            self.roll=input("Enter your Roll no.: ")
            self.age=input("Enter your Age: ")
            Student.count+=1
    print()
    def display(self,x):
        for i in range(x):
            print("Name:",self.name)
            print("Roll no.:",self.roll)
            print("Age:",self.age)

s=Student()
a=int(input("No. of Students: "))
s.get(a)
s.display(a)
print(Student.count)'''


'''class TestClass:
    def __init__(self):
        self.name=None
        self.roll=None
        self.dept=None
    def __del__(self):
        print("Destructor is called ")

objs=list()
a=int(input("Enter the range: "))
for i in range(a):
    objs.append(TestClass())

print(objs)

for i in range(a):
    objs[i].name=input("Name: ")
    objs[i].roll=input("Roll no.: ")
    objs[i].dept=input("Deptartment: ")


print()
print(1,"to",(a))
b=int(input("Enter the no.: "))
print(objs[(b-1)].name)
print(objs[(b-1)].roll)
print(objs[(b-1)].dept)'''

class Store:
    def Products(self,name,code,price):
        self.name=name
        self.__code=code
        self.__price=price

product=list()
for i in range(5):
    product.append(Store())

    product[0].name="UNI PIN"
    product[0].code="49 02778 915262"
    product[0].price=110
    product[1].name="PaperKraft"
    product[1].code="02252005"
    product[1].price=195
    product[2].name="Joy"
    product[2].code="123 321"
    product[2].price=10
    product[3].name="MacBook"
    product[3].code="AppleMac123"
    product[3].price=100000
    product[4].name="Classmate"
    product[4].code="Class123"
    product[4].price=70
    product[5].name="Samsung"
    product[5].code="Sam 123"
    product[5].price=400

print(product)

