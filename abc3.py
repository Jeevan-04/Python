for i in range(1,7):
    for k in range(7,i,-1):
        print('  ',end='')
    for j in range(0,i):
        print('* ',end='')
    for l in range(i-1,0,-1):
        print('* ',end='')
    for m in range(6,i,-1):
        print('  ',end='')
    for n in range(6,i,-1):
        print('  ',end='')
    for j in range(0,i):
        print('* ',end='')
    for l in range(i-1,0,-1):
        print('* ',end='')
    print()