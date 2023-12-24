#WAP to accept length and width of rectangle and give perimeter and area
length=int(input("Enter the length: "))
width=int(input("Enter the width: "))
area=length*width
perimeter=2*(length+width)
print("The Perimeter and Area of rectangle with length ",length," & width ",width," is: ",perimeter," & ",area," respectively.")