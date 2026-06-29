'''Count the number of prime numbers in a given range'''
#input range from user
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
#loop through the range and count prime numbers
count = 0
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            count += 1
#display the result
print(f"The number of prime numbers between {start} and {end} is: {count}")
