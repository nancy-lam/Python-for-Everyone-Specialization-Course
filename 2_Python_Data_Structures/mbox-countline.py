# Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Y ou will parse the From line using split() and print out the second word in the line
# (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.

count = 0
with open('mbox-short.txt') as file:
    for line in file:
        if line.startswith('From'):
            count += 1
            lsplit = line.split()[1]
print(f'There were {count} lines start with \'From\'')
