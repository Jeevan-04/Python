'''WAp to print index at which the particular valuee exist. if the value exist att multiple locations in the list print all the indices.
also count the number of times that value is repeated in the list'''
a=[1,5,8,7,4,3,5,1,5,2,5]
b=len(a)
'''for i in range(b):
    print("index no:",i," = ", a[i])'''


c=int(input("Enter the number: "))
i=0
count=0
while i<len(a):
    if c==a[i]:
       print(c,"found at location", i)
       count+=1
    i+=1
print(c,"appears",count,"times in the list")