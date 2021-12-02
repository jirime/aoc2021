f = open("input2.txt", "r")

horizontalni = 0
hloubka = 0

for i in f:
    smer, vzdalenost = i.split()
    vzdalenost = int(vzdalenost)
    #print("{}, {}".format(smer, vzdalenost))
    if smer == "forward":
        horizontalni += vzdalenost
    elif smer == "up":
        hloubka -= vzdalenost
    elif smer == "down":
        hloubka += vzdalenost
    else:
        print("Tohle by se nemelo stat")

print(horizontalni * hloubka)
