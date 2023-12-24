a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

for i in range(a, b):
    if i == 0 or i == 1:
        continue
    count = 1
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            count = 0
            break
    if count == 1:
        print(i, end=" ")
