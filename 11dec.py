'''def fun_name(name,age):
    #print(name)
    #print(age)
    z=name+age
    print(z)

#a=input("Name: ")
#b=input("Age: ")
fun_name(2,age=13) #working
fun_name(age=13,2) #Not working'''

#print(print()) #print() -->returns none

'''def main():
    a=10
    b=55
    print("in function main........dir() =",dir())
    result=absdiff(a,b)
    print("The absolute value of ", a ,"-", b, " = ", result)

def absdiff(x,y):
    print("in function absdiff.........dir() =",dir())
    if x>y:
        z=x-y
    else:
        z=y-x
    return z

main()'''

'''def distance(x1,x2,y1,y2):
    print((((x2-x1)**2)+((y2-y1)**2))**0.5)
distance(1,4,2,6)'''

'''def area():
    r=distance(1,4,2,6)
    print("Area of the given circle: ",3.14*(r**2))
def distance(x1,x2,y1,y2):
    return((((x2-x1)**2)+((y2-y1)**2))**0.5)
area()'''

'''#***important
#Recursion
def fact(n):
        
    if n==0:
        return 1
    else:
        factorial=n*fact(n-1)
        return factorial
try:
    a=int(input("Enter the number: "))
    print(fact(a))
except:
    print("Invalid Input")'''