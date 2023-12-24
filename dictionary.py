#dictionary is {key:value}
'''{dictionaries}
    set of key alue pairs 
    and are mutable'''
d={1:'hello','two':2,'blah':[1,2,3],'new':{3:'hii','no':4}}
j={}
print(d)
print("blah=", d['blah'])
print("two=", d['two'])
print("1=", d[1])
d['blah']=['a','b','c','d'] #modified
print("New- 'blah' = ", d['blah'])
d[5]='new entry'
print("Added d=", d) #added
del(d['blah'])
print("deleted =", d)

print("list of keys: ",d.keys())
print("list of value: ",d.values())
print("update: ",d.update(j))
#print("pop: "d.pop(1)) #later do
print("clear all: ",d.clear())