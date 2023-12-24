'''#Single_Inheritance
class Parent():
    def add(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
class Child(Parent):
    def takevalues(self):
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        c=self.add(a,b)
        print(c)
obj=Child()
obj.takevalues()'''

'''#Single_Inheritance
class Parent():
    def areea(self):
        self.area=self.a*self.b
        return self.area
class Child(Parent):
    def takevalues(self):
        x=int(input("Enter the first number: "))
        y=int(input("Enter the second number: "))
        self.a=x
        self.b=y
obj=Child()
obj.takevalues()
print(obj.areea())
obj2=Child()'''

'''#Single_Inheritance
class Parent():
    def area(self,x,y):
        print("Area: ",self.x*self.y)
class Child(Parent):
    def takevalues(self):
        self.x=int(input("Enter the first number: "))
        self.y=int(input("Enter the second number: "))
obj=Child()
obj.takevalues()
obj.area(obj.x,obj.y)'''

'''#Area of different cases according to the no. of lengths given by the user
class Area:
    a=[]
    def square(self):
        print("Area of Square: ",self.a[0]*4)
    def rectangle(self):
        print("Area of Rectangle: ",self.a[0]*self.a[1])
    def Triangle(self):
        self.b=((self.a[0]+self.a[1]+self.a[2])/2)
        self.c=(self.b*((self.b)-(self.a[0]))*((self.b)-(self.a[1]))*((self.b)-(self.a[2])))**0.5
        print("Area of Triangle: ",self.c)

class Input(Area):
    def check(self):
        b=int(input("Enter the number of lengths: "))
    
        if b<=0 and b>3:
            print("Invalid Input !")
        else:
            for i in range(b):
                c=float(input("Enter the length: "))
                Area.a.append(c)
                d=len(Area.a)
    
        if d == 1:
            Area.square(self)
        elif d==2:
            Area.rectangle(self)
        elif d==3:
            Area.Triangle(self)

obj=Input()
obj.check()'''


'''#Multiple Inheritance
class Letsupgrade:
    a=[["Python","CPP","Java"],["Saurabh sir","Sai sir","Prasad sir"],["12:00","15:00","02:00"]]
class ITM:
    b=[["Soft skills","Business Studies","Entreprenuership"],["Sakshi ma'am","Sheetal ma'am","Sumit sir"],["16:00","19:00","23:00"]]
class Btech(Letsupgrade,ITM):
    def courses():
        print("LetsUpgrade")
        for i in range(3):
            print(i+1,"=",Letsupgrade.a[0][i],"--",Letsupgrade.a[1][i],"--",Letsupgrade.a[2][i])
        print()
        print("ITM")
        for i in range(3):
            print(i+4,"=",ITM.b[0][i],"--",ITM.b[1][i],"--",ITM.b[2][i])
    def choice(self):
        self.x=input("Enter the subject no.: ")
'''


'''class Grandfather():
    def __init__(self):
        self.name="omkarnath shastri"
        self.asset=15
        self.property=20
class Father(Grandfather):
    def __init__(self):
        super().__init__()
        self.namefather="vidyadhar"+" "+ self.name
        self.assetfather=self.asset +5
        self.propertyfather=13
class Child(Father):
    def __init__(self):
        super().__init__()
        a=input("Enter the name of the child.: ")
        self.namechild="Pandit "+" "+a+" "+ self.namefather
        print("Hii, ", self.namechild)
        print("Your total Asset is: ",self.assetfather)
        print("Inherited: ",self.asset)
        print("Purchesed: ",self.property + self.propertyfather)


obj=Child()'''
    
'''class Grandfather():
    def __init__(self):
        self.name="omkarnath"
        self.asset=15
        self.property=20
class Father(Grandfather):
    def __init__(self):
        super().__init__()
        self.namefather="Shantanu"+" "+ self.name
        self.assetfather=self.asset +5
        self.propertyfather=13
class Husband():
    def __init__(self):
        self.namehusband="vichitravirya"
        self.assethusband=35
        self.propertyhusband=63
class Daughter_wife(Father,Husband):
    def __init__(self):
        super().__init__()
        Husband.__init__(self)
        a=input("Enter the name of the child.: ")
        self.namechild="Devi "+" "+a+" "+ self.namehusband
        print("Hii, ", self.namechild)
        print("Your total Asset is: ",self.assetfather + self.assethusband ,"Gold Bricks weighing 50 kg each")
        print("Inherited: ",self.asset + self.assethusband ,"Gold Bricks weighing 50 kg each")
        print("Purchesed: ",self.property + self.propertyfather + self.propertyhusband ,"Gold Bricks weighing 50 kg each")


obj=Daughter_wife()'''

#Design a library catalogue system using inheritance.
#Take a base class (Library Item) and Derived classes (Book,DVD & journal).
# Each derived class should have unique attributes and methods 
# and system should support check in and check out system.
from datetime import datetime
from datetime import date
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
class Library():
    def issue():
        print("Issue Date:", today)
        print("Issue Time =", current_time)
    def returning():
        print("Returning Date:", today)
        print("Returning Time =", current_time)
class Books(Library):
    a=[["Mahabharata","krishna dwaipayana vyasa",20],["Ramayana","vamiki",15],["dnyaneshwari","dnyaneshwar",10],["Ramcharitmanas","Tulsidas",25],["abhijnyana Shakuntalam","Kalidas",10],]
    def book():
        print("")

print("Issue Date:", today)
print("Issue Time =", current_time)