f = open("input1.txt", "r")

j = 0
count = 0

for i in f:
    i = int(i)
    if i > j:
        count += 1
    j = i

print(count - 1)