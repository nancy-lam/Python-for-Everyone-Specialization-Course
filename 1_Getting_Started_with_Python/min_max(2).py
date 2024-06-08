list = []

while True:
    inp = input('Enter number: ')
    if inp == 'done':
        break
    try:
        num = int(inp)
        list.append(num)
        list.sort()
    except:
        print('Enter number, not a word!')
        continue

print('Smallest number is ', list[0])
print('Largest number is ', list[-1])
