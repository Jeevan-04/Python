'''#1.WAP function to find the maximum of three numbers
def look(a,b,c):
    print("Maximum no.:",max(a,b,c))

look(3,5,2)'''

'''#2.WAP function to sum all the numbers in a list.
def sum(x):
    a=[]
    total=0
    for i in range(x):
        print(i+1,end=' ')
        b=float(input("Enter the number:. "))
        a.append(b)
        total+=a[i]
    print(total)

sum(3)'''

'''#3.WAP function to multiply all the numbers in a list.
def multiply(x):
    a=[]
    total=1
    for i in range(x):
        print(i+1,end=' ')
        b=float(input("Enter the number:. "))
        a.append(b)
        total*=a[i]
    print(total)

multiply(3)'''

'''#4.WAP to reverse a string
str="12345abcd"
a=str[::-1]
print(a)'''

'''#4.2.WAP to reverse a string
str="12345abcd"'''

'''#5.WAP to calculate the facorial of a number.(a non negative integer).
def fact(n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)
print(fact(3))'''

'''#6.WAP to find square and cube 
def cube(n):
    print(n**3)
def square(n):
    print(n**2)
cube(3)
square(3)'''

'''#7.WAP to take the list and returns another list with distinct elements from the first list
#sample input:[1,2,3,3,3,3,4,5]
#sample outcome:[1,2,3,4,5]
a=[1,2,3,3,3,3,4,5]
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])

print(b)'''

'''#8.WAp function that accepts a string and counts the upper and lower cases
#"Today is My Best Day"
str='Today is My Best Day'
upper=0
lower=0
for i in str:
    if i>='a' and i<='z':
        lower=lower+1
    elif i>='A' and i<='Z':
        upper=upper+1
print(upper)
print(lower)'''

#9.WAP Perfect or not ?
a=int(input("Enter the number: "))
b=[]
b.append(a)
i=0
for i in range(a):
    if a%i == 0:
        b.append()
    else:
        continue
    i+=1
print(b)


'''#WAP to check plaindrome
str="MADAM"
if str[::-1] == str:
    print("Is Palindrome")
else:
    print("Not a Palindrome")'''