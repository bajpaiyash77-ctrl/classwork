'''Program for factors of a number'''
#input number from user
number = int(input("Enter a number to find its factors: "))
#display of input
if number == 0:
    print("0 has infinite factors.")
elif number < 0:
    num = -number
    print(f"The factors of {num} are: ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i,",",-i ,end=" ")
else:
    print(f"The factors of {number} are: ")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end=", ")