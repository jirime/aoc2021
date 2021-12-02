f = open("input2.txt", "r")

horizontalni = 0
hloubka = 0
aim = 0
print(type(aim))
print("tu som")

for i in f:
    smer, vzdalenost = i.split()
    vzdalenost = int(vzdalenost)
    print("aim {}, horizontalni {}, hloubka {}".format(aim, horizontalni, hloubka))
    print("smer {}, vzdalenost {}".format(smer, vzdalenost))
    if smer == "forward":
        horizontalni += vzdalenost
        hloubka = hloubka + (aim * vzdalenost)
    elif smer == "up":
        aim -= vzdalenost
    elif smer == "down":
        aim += vzdalenost
    else:
        print("Tohle by se nemelo stat.")

print("horizontalni: {}, hloubka {}, aim {}".format(horizontalni, hloubka, aim))
print(horizontalni * hloubka)
