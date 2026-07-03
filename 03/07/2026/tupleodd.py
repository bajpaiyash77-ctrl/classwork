'''Display of odd numbers in a tuple.'''
number=[]

print("Enter 15 numbers: ")
for i in range(15):
    numbers=int(input())
    number.append(numbers)

t1=tuple(number)
print("The numbers in the tuple are: ")
for i in t1:
    print(i)

print("----------------------------")
print("The odd numbers in the tuple are: ")
for i in t1:
    if i%2!=0:
        
        print(i,end=" ")
