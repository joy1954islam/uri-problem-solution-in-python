tst = int(input())
while tst>=1:
    dif=int(input())
    if(dif<2015):
        year = 2015 - dif
        print("%d D.C." %year)
    else:
        year = dif - 2014
        print("%d A.C." %year)
    tst=tst-1
