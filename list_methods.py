#To demonstrate different methods of list.
'''Step 1: Create a list'''
a=[1,'hello',3.8,5,'a']
print(a)

a.append(15)
print("append", a)

a.extend([20,'hii',36])
print("extend", a)

a.pop(1)
print("pop with i=1", a)

a.pop()
print("pop with defalt ", a)

a.reverse()
print("reverse ", a)

a.insert(2,'hello')
print("insert",a)

a.remove('hello')
print("remove", a)

b=[4,5,3,7,2,6,1]
b.sort()
print("sort", b)

b.sort(reverse=True)
print("descending ",b)