#array
x=[1,2,3]
print("Print Original X",x)
y=x
print("Values of x in y",y)
x[1]=15
print("Reassigned in index 1",x)
print("To check is it affects here ",y)
z=x.append(12)
m=y.append(8)
print("append with 12",x) # to check if append happens in the vice versa format
z==None
print(z) 
print(y)
x=x+[9,10]
y=x
print(x)
print(y)
'''a new list is been created when concatenated butin append its in the main one'''