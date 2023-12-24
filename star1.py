for i in range(9):
    for j in range(13):
        if i==2 or i==6 or i+j==6 or j-i==6 or i-j==2 or i+j==14:
            print("*",end='')
        else:
            print(" ",end='')
    print()