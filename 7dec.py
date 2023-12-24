'''#WAP to unpack a tuple in several variables.
a=(1,2,3,4)
b=97
for i in range(len(a)):
    print(chr(b+i),"=",a[i])'''

'''#WAP tp remove empty tuple(s) from a list of tuples
  #Sample Date: [(),(),('',),('a','b'),('a','b','c'),('d')]
  #Expected outcome: [('',),('a','b'),('a','b','c'),'d']
a=[(),(),('',),('a','b'),('a','b','c'),('d')]
for i in range(len(a)):
    if a[i]==():
        a.pop(i)

print(a)
'''

'''#WAP tp remove empty tuple(s) from a list of tuples
  #Sample Date: [(),(),('',),('a','b'),('a','b','c'),('d')]
  #Expected outcome: [('',),('a','b'),('a','b','c'),'d']
#list comprehension
a=[(),(),('',),('a','b'),('a','b','c'),('d')]
a=[t for t in a if t !=()]
print(a)'''

'''#WAP to unzip a list of tuples into individual lists
a=[('a','b'),('a','b','c'),('d')]
for i in range(len(a)):
    print(chr(97+i),"=",list(a[i]))
'''

'''#WAP to calculate parking charges of a vehicle.Enter the type of vehicle as a type of character.
#eg. 'c' for car and 'b for bus, etc...And number of hours and then calculate charges as given below
#Truck/bus = $20 /hr
#Car= $10 /hr
#scooter/Cycle/Bike = $5/hr

print("Truck= T,  Bus=B,  Scooter=S,  Car=C,  Bike=I,  Cycle=Y")
a=(input("vehicle: ")).upper()
b=int(input("Period: "))
charge={'T':20,'B':20,'C':10,'S':5,'Y':5,'I':5}
print("Charges:",a," for ",b," :",charge[a]*b)'''

'''#WAP to 
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
#|Vehicle name| Rate till 3 /hrs| Rate after /hrs|
#|_ _ _ _ _ _ | _ _ _ _ _ _ _ _ | _ _ _ _ _ _ _ _|
#|Truck/Bus   |       20        |     30         |
#|Car         |       10        |     20         |
#|Cycle       |       5         |     10         |
#|scooter/Bike|       5         |     10         |
#|_ _ _ _ _ _ | _ _ _ _ _ _ _ _ | _ _ _ _ _ _ _ _|

a=input("Vehicle: ")
charge1={'T':20,'B':20,'C':10,'S':5,'Y':5,'I':5}
charge2={'T':30,'B':30,'C':20,'S':10,'Y':10,'I':10}
time1=input()'''

'''#WAP that creates a dictionary of cubes of odd numbers in the range 1 to 10.
#a=[]
#for i in range(11):
#    if i %2 !=0:
#        a.append(i)
#print(a)
#
#b=[]
#for i in range(len(a)):
#    c=a[i]*a[i]*a[i]
#    b.append(c)
#
#print(b)
#
#for i in range(len(a)):
    


d={}
for i in range(1,10,2):
    d[i]=i**3
print(d)'''

'''# Nested Tuple
# WAP to print the name of the topper and his/her marks in four subjects 
# wherein the marks are specified as a list in the tupple topper.

students=[]
c=[]
for i in range(5):
    a=input("Name of the student")
    for j in range(4):
        b=int(input("Marks:"))
        c.append(b)'''

'''#WAP to add a tuple to a list.
a=[1,3,5,6]
b=(67,46,78)
c=list(b)
print(a+c)
print(tuple(a+c))'''

'''#WAP to find size of the program.
a=(66,77,88,'car','roy',87.65)
print(len(a))'''

#WAP to create list of tuples from list of numbers and its cube in each tuple.
d=[]
for i in range(2,7):
    d.insert(i,i**3)

c=[0,0,0,0,0]
a=[2,3,4,5,6]
for i in range(len(d)):
    c[i]=a[i],d[i]

print(c)