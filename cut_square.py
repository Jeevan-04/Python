for i in range(1,5):
    for k in range(5,i,-1):
        print('  ',end='')
    for j in range(0,i):
        print('* ',end='')
    for l in range(i-1,0,-1):
        print('* ',end='')
    print()
for i in range(5,0,-1):
    for k in range(i,5,+1):
        print('* ',end='')
    for j in range(i,0,-1):
        print('  ',end='')
    for l in range(0,i-1,+1):
        print('* ',end='')
    print()
