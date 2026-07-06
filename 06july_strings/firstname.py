name=input("Enter your first name: ")
first=[]
for i in name:
    if i>='A' and i<='Z' or i>='a' and i<='z':
        first.append(i)
    else:
        break
print("The new first name is: ", (first))  