'''Calculate the area of a circle'''
#input radius
r = float(input("Enter the radius of the circle: "))
#validation of radius 
if r < 0:
    exit("Radius cannot be negative. Please enter a positive value.")  
#Display the radius
print("The radius of the circle is:", r)
#calculate area
area = 3.14159 * r ** 2

#Display the area   
print("The area of the circle is:", area)
