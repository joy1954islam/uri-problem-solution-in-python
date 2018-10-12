a,b,c=list(map(int,input().split()))
d=a+b+c
if(d>=24):
    d=d-24
if(d<0):
    d=24+d
print(d)