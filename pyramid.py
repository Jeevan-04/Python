for i in range(1,5):
    for k in range(5,i,-1):
        print('  ',end='')
    for j in range(0,i):
        print('* ',end='')
    for l in range(i-1,0,-1):
        print('* ',end='')
    print()