'''count no. of special characters in a sentence '''

#input
sentence = input("Enter a sentence: ")

#count special characters
special_count = 0
for char in sentence:
    if char.isalnum():
        pass
    elif char.isspace():
        pass
    else:
        special_count += 1
print("The number of special characters in the sentence is: ", special_count)