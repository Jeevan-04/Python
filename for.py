#Addition of first ten numbers
sum=0
for i in range(1,11):
    sum+=i
print("sum is",sum)
num=0

for j in range(1,11,2):
    num+=j
print("sum is",num)

numb=0
a=int(input("Enter the range 1: "))
b=int(input("Enter the range 2: "))
c=int(input("Enter the difference: "))
for k in range(a,b,c):
    numb+=k
print("sum is",numb)