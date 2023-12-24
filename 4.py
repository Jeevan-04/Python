#WAP to how many sunday did you live so far from bith day.
day=input("Birth day: ")
date=int(input("Birth date: "))
year=int(input("Birth year: "))
count=0
for i in range(year, 2023):
    count+=1
print(count*52)