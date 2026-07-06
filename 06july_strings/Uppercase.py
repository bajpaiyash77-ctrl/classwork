'''count no. of uppercase and lowercase letters in a sentence w/o using built-in functions'''
sentence=input("Enter a sentence: ")
uppercase_count=0
lowercase_count=0
for char in sentence:
    if 'A' <= char and char <= 'Z':
        uppercase_count += 1
    elif 'a' <= char and char <= 'z':
        lowercase_count += 1
    else:
        pass

print("The number of uppercase letters in the sentence is: ", uppercase_count)
print("The number of lowercase letters in the sentence is: ", lowercase_count)