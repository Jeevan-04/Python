#while loop demonstration
n=int(input("Enter the nth term: "))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1 #update counter
print("The sum is ",sum)