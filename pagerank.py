from collections import Counter
lineList = []

# read file line by line
file = open( "links.srt", "r")
lines = file.readlines()
file.close()
print(len(lines))
targets = []
for i in lines:
    for j in range(len(i)):
        if(i[j] == '\t'):
            targets.append(i[j+1:])

count = Counter(targets)
print(len(count))
print(count.most_common(10))
# print(count)


