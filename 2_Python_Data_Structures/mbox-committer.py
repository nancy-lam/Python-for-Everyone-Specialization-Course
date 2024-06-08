# Write a program to read through the mbox-short.txt
# and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the
# sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

count = 0
dict = {}
with open('mbox-short.txt') as file:
    for line in file:
        if not line.startswith('From '): continue
        count += 1
        emails = line.split()[1]
        dict[emails] = dict.get(emails, 0) + 1
    print(dict)
print()

# Create a list of sender
lsd = []

# and a list to count their commitment
lcm = []

for sender, commit in dict.items():
    lsd.append(sender)
    lcm.append(commit)
    # Maximum of commit
    mcm = max(lcm)

position = lcm.index(mcm)

print(f'The most prolific committer is {lsd[position]}: {mcm}')





        
                


        