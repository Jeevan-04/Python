'''for i in range(1,5):
    for k in range(5,i,-1):
        print('  ',end='')
    for j in range(0,i*2-1):
        if j==0 or j==1*2-2:
         print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(5,1,-1):
    for k in range(i,5,1):
        print('  ',end='')
    for j in range(i,0,-5):
        print('* ',end='')
    print()'''
for i in range(5):
    for j in range(5):
        if i+j==2 or j-i ==2 or i-j==2 or i+j==6:
            print("* ",end='')
        else:
            print(end="  ")
    print()