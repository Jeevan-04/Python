#Day.1.lab.1
'''Aim: Write a Program to demonstrate the following operators in python with example:
        (i)Arithmetic (ii)relational (iii)bitwize (iv)assignment (v)assignment
        (vi)logical (vii)ternary (viii)membership (ix)identity'''

'''Arithmetic Operators'''
#addition
def add(a,b):
    return a+b
#substraction
def sub(a,b):
    return a-b
#division
def div(a,b):
    return a/b
#multiplication
def mult(a,b):
    return a*b
#mod
def mod(a,b):
    return a/b
#exponential
def expo(a,b):
    return a**b
#floor division
def floor(a,b):
    return a//b
    

print("lets understand the operations")

print("""
(i)Arithmetic (ii)relational (iii)bitwize (iv)assignment (v)assignment
(vi)logical (vii)ternary (viii)membership (ix)identity
      """)
choice_op=str(input("The type of operation: "))

match choice_op:
    case "1":
        choice_ar=str(input("The type of arithmetc operation: "))
       match choice_ar:
            case