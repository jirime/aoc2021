f = open("input1.txt", "r")

j, k, l = 1000, 1000, 10000

count = 0

#def summ(a, b, c):


for i in f:
    i = int(i)
    prvni = (j, k, l)
    druha = (k, l, i)
    if sum(prvni) < sum(druha):
        count += 1
    j = k
    k = l
    l = i

print(count)