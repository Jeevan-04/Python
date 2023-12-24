'''def hello():
    print('Hello World')
hello()'''

'''def hello():
    return('Hello World')
str=hello()
print(str)'''

'''def addition(a,b):
    return a+b

str=addition(1,2)
print(str)'''

'''#WAP to use all arithmetic operations in a single program.
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def exponent(a,b):
    return a**b
def floor(a,b):
    return a//b
def mod(a,b):
    return a%b
def square(a):
    return a*a
def root(a):
    return int(a**0.5)


b=float(input("Enter the first number: "))
c=float(input("Enter the second number: "))
print('What operation would you perform ?')
a=int(input("""1.Addition \n 2.Subtraction  \n 3.Multiplication \n 4.Division \n 5.Exponent \n 6.Floor \n 7.Mod \n 8.Square \n 9.Root.\n"""))
if a == 1:
    d=addition(b,c)
    print(d)
elif a == 2:
    d=subtraction(b,c)
    print(d)
elif a == 3:
    d=multiplication(b,c)
    print(d)
elif a == 4:
    d=division(b,c)
    print(d)
elif a == 5:
    d=exponent(b,c)
    print(d)
elif a == 6:
    d=floor(b,c)
    print(d)
elif a == 7:
    d=mod(b,c)
    print(d)
elif a == 8:
    d=square(b,c)
    print(d)
elif a == 9:
    d=root(b,c)
    print(d)
else:
    print("Invalid Input !")
    '''

'''#Dynamic Argument Passing
def my_function(*args):
    for i in args:
        print(i)
    
my_function('hello',1,3,4,[5,6,7])'''

'''#positional arguments
def my_function(name,rollno):
    print(name)
    print(rollno)

my_function('lakshya',46)'''

'''#Keyword based arguments
def my_function(name,rollno):
    print(name)
    print(rollno)

my_function(rollno=46,name='lakshya')'''

'''#display all submissions of all argumenets passed and sum of numbers ad average of all numbers.
def addition(*args):
    a=0
    b=0
    for i in args:
        a+=i
        b+=1
    
    print("Arguments Passed: ",end='')
    for j in args:
        print(j,end=" ")
    
    print()
    print("Total: ",a)
    print("Average: ",a/b)

addition(5*3+4)'''



'''#WAP to create a list of elements and accessing each element and adding them.
def todo():
    a=int(input("Enter the length: "))
    b=[]
    sum=0
    for i in range(a):
        c=int(input("Enter the number: "))
        b.append(c)
    print("Created List: ",b)

    print("All elements: ")
    for i in range(len(b)):
        sum+=b[i]
        print(i," = ",b[i])

    print("sum: ",sum)

todo()'''

'''#WAP to use *args converted to list and accessing each element and adding them all.
def to(*args):
    l=[]
    sum=0
    for i in args:
        l.append(i)
    
    print("Arguments Passed: ",end='')
    for j in args:
        print(j,end=" ")

    print() 
    print("args: ",args)

    print("list: ",l)

    for k in range(len(l)):
        sum+=l[k]
    
    print("sum: ",sum)

to(1,2,3,4)'''

'''#ARGS
def my_function(a,b, *args):
    print("a: ",a)
    print("b: ",b)
    print("args: ",args)

my_function(1, 5, 2, b=3, a=4)'''

'''#KWARGS
def function(**kwargs):
    print(kwargs)

function(name='lakshya',rollno=46)'''

'''#KWARGS AND ARGS TOGETHER
def function(*args,**kwargs):
    print("args: ",args)
    print("kwargs: ",kwargs)

    for i in range(len(args)):
        print(i,"=",args[i])
    for j in kwargs:
        print(j," = ",kwargs[j])

function('hello','itm',name='lakshya',rollno=46)'''

'''#Welcome Note
def welcom():
    c=input("What is your Name ? ")
    print("Welcome",c,"! to ITM")

welcom()'''

'''#Details with KWARGS
def details(**kwargs):
    print() 
    for i in kwargs:
        print(i,"=",kwargs[i])

a=input("Name: ")
b=input("Age: ")
c=input("Email: ")
d=input("Roll no: ")
details(Name=a,Age=b,Email=c,Rollno=d)'''

'''#Deatils-2
def details(**kwargs):
    print() 
    for i in kwargs:
        print(i,"=",kwargs[i])

print("What details would you like to share ? ")
q=input("1.name \n 2.age \n 3.email \n 4.rollno (1 4 (default))")
if q=='2 3':
    a=input("Name: ")
    b=input("Age: ")
    c=input("Email: ")
    d=input("Roll no: ")
elif q=='3':
    a=input("Name: ")
    b="NA"
    c=input("Email: ")
    d=input("Roll no: ")
elif q=='2x':
    a=input("Name: ")
    b=input("Age: ")
    c="NA"
    d=input("Roll no: ")
else:
    print("invalid input !")

details(Name=a,Age=b,Email=c,Rollno=d)'''

'''#local and global
variable=4#---> Global

def function():
    #global variable #---> makes the variable global in the function using keyword global so that we can modify.
    variable=3
    print(variable) #---> Local

function() #----> scope of local variable ends after this.
print(variable) #---> Global'''

'''#local, Global & Non Local
variable=10
def fun():
    variable=3
    print(variable) #----> local
    def fun2():
            #nonlocal variable
            variable=4
            print(variable) #----> Non local
    print(variable)
    fun2()

fun()
print(variable) #----> global'''

