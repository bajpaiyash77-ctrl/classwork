'''accept a sentence from user and stores the frequency of each word.'''
'''Additionaly display the most frequently occuring word in the sentence.'''
'''Display all words in alphabetical order '''

#input a sentence from user
sentence = input("Enter a sentence: ")

#split the sentence into words
words = sentence.split()

#count the frequency of each word
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

#display the frequency of each word
print("The frequency of each word in the sentence is: ")
for word, frequency in word_frequency.items():
    print(word, ":", frequency)

#find the most frequently occuring word
most_frequent_word = max(word_frequency, key=word_frequency.get)
print("The most frequently occuring word in the sentence is: ", most_frequent_word)

#display all words in alphabetical order
sorted_words = sorted(word_frequency.keys())
print("The words in alphabetical order are: ")
for word in sorted_words:
    print(word)


