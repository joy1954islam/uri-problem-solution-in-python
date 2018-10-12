n=int(input())
for i in range(n):
    a=int(input())
    c=int(a/2)
    d=0
    for b in range(1,c+1):
        if(a%b==0):
            d+=b
    if(d==a):
        print("{} eh perfeito".format(a))
    else:
        print("{} nao eh perfeito".format(a))