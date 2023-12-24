#dictionary is {key:value}
'''{dictionaries}
    set of key alue pairs 
    and are mutable'''
d={1:'hello','two':2,'blah':[1,2,3],'new':{3:'hii','no':4}}
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