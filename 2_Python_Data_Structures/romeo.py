# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

list_of_words = []
with open('romeo.txt') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word in list_of_words: continue
            list_of_words.append(word)
            list_of_words.sort()
print(list_of_words)