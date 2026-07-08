'''You are required to create a Python module named twodfigures.py that contains functions to perform the following calculations for different two-dimensional shapes:

Triangle
Calculate Area
Calculate Perimeter
Circle
Calculate Area
Calculate Circumference (Perimeter)
Square
Calculate Area
Calculate Perimeter
Rectangle
Calculate Area
Calculate Perimeter'''

# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Function to calculate the perimeter of a triangle
def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return 3.14159 * radius * radius

# Function to calculate the circumference (perimeter) of a circle
def calculate_circle_circumference(radius):
    return 2 * 3.14159 * radius

# Function to calculate the area of a square
def calculate_square_area(side):
    return side * side

# Function to calculate the perimeter of a square
def calculate_square_perimeter(side):
    return 4 * side

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Function to calculate the perimeter of a rectangle
def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)
