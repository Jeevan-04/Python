# #1. WAP to declare, assign and print the string (Different ways)
# #Hello World, How are you?
# #i.using single quotes 'string'
# #ii.using double quotes "string"
# #iii.using triple quotes '''string'''
# #iv.using triple double quotes """string"""
# #v.using triple double quotes allows to assign (multi-line string)
# print('Hello World, How are you?')
# print("Hello World, How are you?")
# print('''Hello World, How are you?''')
# print("""Hello World, 
# How are you?""")

'''#2.WAP to access and print characters from the string 
#"Hello World"
#1.print complete string
#2.print first character
#3.print second character
#4.print last character
#5.print second last character
#6.print characters from 0th to 4th index
#7.first 5 characters
#8.print 2nd index to 2nd last index
#9.Print string character by character
str="Hello World"
#1
print('1',str)
#2
print('2',str[0])
#3
print('3',str[1])
#4
print('4',str[-1])
#5
print('5',str[-2])
#6
print('6',str[0:4])
#7
print('7',str[0:6])
#8
print('8',str[2:-1])
#9
print('9')
for i in range(len(str)):
    print(str[i])'''


'''#3.WAP to find uncommon words of two string
a="hello world, how are you"
b="What is your name world ?"
c=a.split(" ")
d=b.split(" ")
# if len(c)>len(d):
#     for i in range(len(c)):
#         print(b.find(c[i]))
#         print("found")
# else:
#     for i in range(len(d)):
#         print(a.find(d[i]))
#         print("found")

import re
i=0
while i in c:
    if re.match(c[i],b,flags=re.I):
        print("Found")
    else:
        print("Not found")
    i+=1'''


# #4.Binary or not
# a=input("Enter.: ")
# if all (bit=='0' or bit=='1' for bit in a):
#     print("binary")
# else:
#     print("non binary")

#5.least frequent character
str="hello world"
a=[]
count=0
for i in range(len(str)):
    a+=str[i]
#6.removing ith character fro string
#7.class employee
    #1.id:1
    #name:pankaj
    #city:delhi
    #gender:male
    #salary:55000
