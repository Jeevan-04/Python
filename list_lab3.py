'''list=[10,20,30,40,50]
print("The elements in the list 'list' is: ",list)
print()
print("Elements in the list with index location: ")
for i in range (5):
    print(i," - ", list[i])

list2=['mumbai','pune','nashik','new Delhi']
print("The elements in the list 'list' is: ",list2)
print()
print("Elements in the list with index location: ")
for i in range (4):
    print(i," - ", list2[i])

list3=[3,'pune',2,'new Delhi']
print("The elements in the list 'list' is: ",list3)
print()
print("Elements in the list with index location: ")
for i in range (4):
    print(i," - ", list3[i])

a=[10,20,30,40,50,60,70,80,90,100]
print(a)
print("first element: ",a[0])
print("fourth element: ",a[5])
print(a[0:4])

#print list -7 to 3rd element of list
print(a[-7])

#appending
a.append(110)
print("Original: ", a)
print("sorted: ",a.sort())
print("pop: ",a.pop())
print("popped: ",a)

a.remove(80)
print("removed: ",a)

#index inserting 100
a.insert(0,100)
print("insertd: ",a)

#counting of occurance of 100
print("count of 100: ",a.count(100))

#extending an element in a list
a.extend([120,130])
print("extended: ",a)

#reversing the list
a.reverse()
print("reversed: ",a)'''

'''#two list of even and odd from a list
list3=[11,22,33,44,55]
even=[]
odd=[]
b=len(list3)
for i in range(b):
    if list3[i]%2==0:
        even.append(list3[i])
    else:
        odd.append(list3[i])

print("even:", even)
print("odd:",odd)'''
'''
#WAP iterate/traverse a list in a reverse order by three methods using- rever, slicing, insert
list=[10,20,30,40,50]
c=len(list)
list.reverse()
print("reversed: ",list)

print(list[::-1])

a=[]
for i in range(c):
    a.insert(i,list[i])

print("inserted:", a)'''

'''#write a programa to extend a list in python using given apprach
#using + 
list+[70,80]
print("+ :",list)
#using append
list.append(90)
print("append:",list)
#using extend
list.extend([100,120])
print("extend: ",list)
'''
'''#Write a progam to find sum and mean
x=[1,2,3,4]
p=len(x)
y=0
for i in range(p):
    y+=x[i]

print("sum: ",y)
print((/2))'''

'''#WAP to delete all duplicate values
list=[10,11,13,12,14,12,11,13,10,11]
p=len(list)
a=[]
for i in range(p):
    if list[i] not in a:
        a.append(list[i])
    #else:
        #continue

print(a)'''

'''#WAP to add two matrices using the nested list

x=[[2,5,4],
   [1,3,9],
   [7,6,2]]
y=[[1,8,5],
   [7,3,6],
   [4,0,9]]
k=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        k[i][j]=x[i][j]+y[i][j]
    print(k[i])
'''

#