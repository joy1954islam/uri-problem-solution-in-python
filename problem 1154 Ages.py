b=0
d=0
while(True):
    try:
        n=int(input())
        if(n<0):
            break
        else:
            b=b+n
            d=d+1
    except EOFError:
        break
c=b/d
print("%0.2f"%c)