'''Display of odd numbers in a tuple.'''
number=[]
for i in range(15):
    numbers=int(input("Enter number: "))
    number.append(numbers)

for i in range(15):
    print("the numbers in the tuple are: ",i)

t1=tuple(number)
for i in t1:
    if i%2!=0:
        print("the odd numbers in the tuple are: ",i)