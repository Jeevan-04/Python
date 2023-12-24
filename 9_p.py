#WAP to print multiplication table
num=int(input("Enter the number: "))
for i in range(1,10+1,3):
    result=num*i
    print(num," * ",i," = ",result)