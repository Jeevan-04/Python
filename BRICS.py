'''WAP that defines a list of countries that are member of BRICS
check wether the country is member of brics or not'''
brics=['BRAZIL','RUSSIA','INDIA','CHINA','SOUTH AFRICA']

a=input("Enter the name of country: ").upper()

for i in range(5):
    k='not found'
    if a==brics[i]:
        k='found'
        print(a, " is a member of BRICS")
        break
        
if k!='found':
    print(a, " is not a member of BRICS")


