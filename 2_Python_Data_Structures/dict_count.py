# Sort and count words in 'romeo.txt' file. Limit by 10

count = {}

with open('romeo.txt') as file:
    for line in file:
        words = line.split()
        for word in words:
            count[word] = count.get(word, 0) + 1

ls = []
for k, v in count.items():
    new = (v, k)
    ls.append(new)

ls = sorted(ls, reverse=True)

for v, k in ls[:10]:
    print(k, v)