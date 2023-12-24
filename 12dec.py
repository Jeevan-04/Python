'''def check(a,b):
    for i in range(len(a)):
        if b==a[i]:
            print(b,"-",i)
str='ITM Skills University'
check(str,'i')'''

'''def check(a,b):
    for i in range(len(a)):
        if b==a[i]:
            print(b,"-",i)
            break
str='ITM Skills University'
check(str,'i')
'''

'''def check(a,b):
    count=0
    for i in range(len(a)):
        if b==a[i]:
            count+=1
    print(count)
str='ITM SKILLS UNIVERSITY'
check(str,'I')'''

'''print("str[0:3]: ",str[0:3])
print("str[0:3:2]: ",str[0:3:2])
print("str[3]",str[2])
print("str[0:3:2]: ",str[-21:])'''
'''for i in range(len(str)):
    print(i,"=",str[i])'''
'''for letter in str:
    print(letter,end='')'''
'''i=0
while i<len(str):
    print(str[i])
    i+=1'''

'''str='ITM SKILLS UNIVERSITY'
print(str.find('S',10,21))
'''


'''def see(chr):
    str="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse 
    cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, 
    sunt in culpa qui officia deserunt mollit anim id est laborum."""
    if str.find(chr)>=0:
        return True
    else:
        return False
a=input("Enter: ")
if see(a) ==True:
    print(a," is present")
else:
    print(a," doesn't exist")
'''
'''#Print all characters of string one, which are present in string two too.
str1="Emerald eyes emanate exuberant energy."
str2="Energetic echidnas explore every edge."
i=0
while str1[i] != '.':
    if str1[i] in str2:
        print(str1[i],end=' ')
    else:
        pass
    i+=1'''


'''str1=input("Enter string 1: ")
str2=input("Enter string 2: ")
if str1>str2:
    print(str1,">",str2)
elif str1<str2:
    print(str1,"<",str2)
else:
    print(str1,"=",str2)'''

'''print("""Hi,"What's up ?" """)'''
'''print(r"""Hi,"What's up ?" """)'''

a=input("Enter the venue: ")
b=input("Enter the area: ")
print("Welcome to {} {}".format(a,b))
print("Welcome to {1} {0}".format(a,b))
