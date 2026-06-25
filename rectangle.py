'''Calculate the area and perimeter of a rectangle'''

# Input length and breadth
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Validate inputs
if length <= 0 or breadth <= 0:
    raise ValueError("Length and breadth must be positive values.")

# Display inputs
print("The length of the rectangle is:", length)
print("The breadth of the rectangle is:", breadth)

# Calculate area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

# Display results
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)