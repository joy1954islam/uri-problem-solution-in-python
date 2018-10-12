st,sm,et,em=list(map(int,input().split()))
ft = et - st;
if(ft < 0):
    ft = 24 + (et - st)
fm = em - sm
if(fm < 0):
     fm = 60 + (em - sm)
     ft=ft-1
if (et == st and em == sm):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(ft,fm))