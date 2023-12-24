#1.WAP to find the sum of first 2000 odd numbers
count=0
sum=0
for i in range (0,2001,1):
    if i%2 !=0:
        count+=1
    if count==1:
        sum+=i

print(sum)