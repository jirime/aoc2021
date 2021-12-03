gamma = ''
epsilon = ''


def spolecne(j):
    f = open("/home/jiri/Dropbox/programovani/puzzles/aoc2021/day3/input3.txt", "r")
    nuly = 0
    jednicky = 0
    pozice = int(j)
    print("pozice je {}".format(pozice))
    for i in f:
        #print("i[pozice] je {}".format(i[pozice]))
        if i[pozice] == '1':
           jednicky +=1
        else:
           nuly += 1
    print("jednicky {}, nuly {}".format(jednicky, nuly))
    print( jednicky * nuly)
    return '1' if jednicky > nuly else '0'


for k in range(len('000100011010')):
    if spolecne(k) == '1':
        gamma += '1'
        epsilon += '0' 
    else: 
        gamma += '0'
        epsilon += '1'

print (int(gamma, 2) * int(epsilon,2))






