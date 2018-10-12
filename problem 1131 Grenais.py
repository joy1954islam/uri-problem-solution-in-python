l = 0
k = 0
j = 0
c = 0
d = 0
e = 0
while True:
    a,b = list(map(int,input().split()))
    if(a>b):
        l=l+1
    if(a<b):
        k=k+1
    if(a==b):
        j=j+1
    c+=a
    d+=b
    e=e+1
    print("Novo grenal (1-sim 2-nao)")
    n = int(input())
    if(n==1):
        continue
    if(n==2):
        break
print("{} grenais".format(e))
print("Inter:{}".format(l))
print("Gremio:{}".format(k))
print("Empates:{}".format(j))
if(l>k):
    print("Inter venceu mais")
if(l<k):
    print("Gremio venceu mais")
if(k==l):
        print("Nao houve vencedor")