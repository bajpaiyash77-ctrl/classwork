'''Multiplication Table generator'''
#input number
number = int(input("Enter a number to generate its multiplication table: "))   
#display of multiplication table
print(f"Multiplication table of {number}:")
for i in range(1, 21):
    result = number * i
    print(f"{number} x {i} = {result}")
    