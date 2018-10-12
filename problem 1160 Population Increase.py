n = int(input())
for i in range(n):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    a = 0
    while (pa <= pb):
        cpa = int((pa * (g1 / 100)))
        cpb = int((pb * (g2 / 100)))
        a += 1
        pa += cpa
        pb += cpb
        if (a > 100):
            break
    if (a > 100):
        print("Mais de 1 seculo.")
    else:
        print("%d anos." % a)