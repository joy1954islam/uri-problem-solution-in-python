a,b=list(map(int,input().split()))
if(a<b):
    time=b-a
else:
    time=b+24-a
print("O JOGO DUROU {} HORA(S)".format(time))