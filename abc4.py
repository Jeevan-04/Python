val=65
for i in range(5,3,-1):
    ch=chr(val)
    for j in range(0,i):
        print(ch,end='')
    val+=1