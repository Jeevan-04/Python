'''1.WAP to create a dictionary with mixed keys and
i.print the keys
ii.print value and 
iii.print key-value pairs
dict={1:"India",'city':'New Delhi','Record':{'id':101,'name':'Amit','Age':21}}'''

'''#1
dict={1:"India",'city':'New Delhi','Record':{'id':101,'name':'Amit','Age':21}}
print(dict.keys())'''

'''#2
dict={1:"India",'city':'New Delhi','Record':{'id':101,'name':'Amit','Age':21}}
for i in dict:
 print(dict[i])'''

'''#3
dict={1:"India",'city':'New Delhi','Record':{'id':101,'name':'Amit','Age':21}}
 print(dict)'''







'''2.WAP for accessing elements from a dictionary.dict
r1={'id':101,'name':'Amit','Age':21}
a.By using Key Name.
b.By using get() method.'''

'''#1
r1={'id':101,'name':'Amit','Age':21}
print(r1['id'])'''

'''#2
r1={'id':101,'name':'Amit','Age':21}
print(r1.get('Age'))'''










'''3, Wap for removing element from a dictionary.  

    i/p:  record={'id':101,'name':'Amit Kumar','Age':21}

    1.By Using Del Keyword.
    2.By using pop.'''


'''#1
record={'id':101,'name':'Amit Kumar','Age':21}
del record['id']
print(record)'''

'''#2
record={'id':101,'name':'Amit Kumar','Age':21}
record.pop('id')
print(record)'''








'''4,Wap to compare two dictionaries in Python?  (By using == operator)

 i/p:  r1={'id':101,'name':'Amit','Age':21}
      r2={'id':101,'name':'Amit','Age':21}
      r3={'id':101,'name':'raheel','Age':26}
'''

'''
r1={'id':101,'name':'Amit','Age':21}
r2={'id':101,'name':'Amit','Age':21}
r3={'id':101,'name':'raheel','Age':26}

if r1['id']==r2['id']==r3['id']:
    print("true")
else:
    print("false")'''


 
 
 
 
'''5,Wap to generate & print dictionary of no & its square like(i,i*i).

   eg {1:1, 2:4, 3:9....}
'''

'''d={}
for i in range(10):
    d.update({i:i*i})
print(d)'''
 




 
'''6,Wap for adding elements to a Empty dictionary on the following 
   
 i/p={ }  

 o/p={0: 'Amit', 1: 'Kumar', 2: 23, 3: 'Delhi', 'marks': (69, 70, 58), 4: {'Nested': {'Name': 'Shivang', 'Age': 24}}}

  1. Adding one element at a time.
  2. Adding multiple values to a key.
  3. Updating an existing Key's Value. 
  4. Adding Nested Key value.'''

d={}
a={0: 'Amit', 1: 'Kumar', 2: 23, 3: 'Delhi', 'marks': (69, 70, 58), 4: {'Nested': {'Name': 'Shivang', 'Age': 24}}}
for i in range(6):
    



''''''