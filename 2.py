#WAP to print first 2000 prime numbers
sum=0
for i in range(0, 2001):
    if i == 0 or i == 1:
        continue
    count = 1
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            count = 0
            break
    if count == 1:
        sum=sum+i
print(sum)