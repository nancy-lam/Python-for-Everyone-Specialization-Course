# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except
#and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.
#Invalid input
#Maximum is 10
#Minimum is 2
    #elif num != int or float : break
    #print("Enter number, not a word!")

max = None
min = None

while True:
    inp = input('Enter number: ')
    if inp == 'done':
        break
    try:
        num = int(inp)
        if min is None:
            min = num
        if min < num:
            min = num
        if max is None:
            max = num
        if max > num:
            max = num
    except:
        print('Enter number, not a word!')
        continue

print(f'Maximum is {max}')
print(f'Minimum is {min}')
