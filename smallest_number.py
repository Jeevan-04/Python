#WAP to find the smallest number in the list
a=int(input("Enter the number of elements: "))
x=[]
for i in range(a):
    b=int(input("Enter the number: "))
    x.append(b)

for i in range(a):
    for j in range(a):
        if x[i]<=x[j]:
            x[i],x[j]=x[j],x[i]

print(x[0])
print(x[a-1])
        