val = 69
for i in range(2, 5):
    val=(69+i-2)
    for k in range(i,5,1):
        print(' ',end='')
    for j in range(0, i+1):
        ch = chr(val-i)
        print(ch,"", end='')
        val = val + 1
    print()

'''n=5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(n - i):
        print(chr(65 + k +i), end=" ")
    print()'''

