x=10
y=3
print(x**y)

# Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)
radius = int(input("Pleas Enter Radius radius \n"))
Area= 3.14*radius**2
print("Area of cirle is ", Area)
#Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than, or  equal to the second number.
a= int(input("Please enter first number \n"))
b= int(input("Please enter Second number \n"))
print(" a is greater than b or a is equal to b" if a >= b else "a less than b")

#Use the ternary operator to find the maximum of three numbers entered by the user
a= int(input("Please enter first number \n"))
b= int(input("Please enter Second number \n"))
c= int(input("Please enter third number \n"))
max = (a if (a>b and a>c) else (b if (b>a and b>c) else c))
print("maximum number is ",max)


#Develop a Python script that calculates the square and cube of a given number.
a= int(input("Please enter the number \n"))
Square = (a**2)
cube = (a**3)
print("The Square of the number is ", Square)
print("The cube of the number is ",cube)