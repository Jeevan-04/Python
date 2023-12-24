#WAP to perform arithmetic operations accepting two operands.
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
num_op=float(input("Enter the operation \n (1)addition \n (2)subtraction \n (3)multiplication \n (4)division \n (5)mod \n (6)exponent \n (7)Floor \n"))
if num_op == 1:
    print(num1," + ",num2,"= ",num1+num2)
elif num_op == 2:
    print(num1," - ",num2,"= ",num1-num2)
elif num_op == 3:
    print(num1," * ",num2,"= ",num1*num2)
elif num_op == 4:
    print(num1," / ",num2,"= ",num1/num2)
elif num_op == 5:
    print(num1," % ",num2,"= ",num1%num2)
elif num_op == 6:
    print(num1,"^",num2,"= ",num1**num2)
elif num_op == 7:
    print(num1," // ",num2,"= ",num1//num2)
