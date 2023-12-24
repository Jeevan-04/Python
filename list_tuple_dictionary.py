#WAP to create lists, tuples and dictionary of 7 elements.(Creation & Printing)
x=[5,2,6,3,4,1,9,7]
y=(4,'hii',"a",9)
a={6:'hello','blah':7,8:'no'}
'''
print(x)
print(y)
print(a)
'''
z=[]

for i in range(8):
    for j in range(8):
        if x[i]>=x[j]:
            x[i],x[j]=x[j],x[i]
print(x)