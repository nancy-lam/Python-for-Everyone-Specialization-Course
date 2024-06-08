# Sort and count words in 'romeo.txt' file. Limit by 10

count = {}

with open('romeo.txt') as file:
    for line in file:
        words = line.split()
        for word in words:
            count[word] = count.get(word, 0) + 1

print(sorted([(v, k) for k, v in count.items()], reverse=True)[:10])