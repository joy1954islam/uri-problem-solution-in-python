d=0
c=0
while(True):
    try:
        if(d==2):
            break
        a = float(input())
        if(a>=0 and a<=10):
            d=d+1
            c=c+a
        else:
            print("nota invalida")
    except EOFError:
        break
b=c/2.00
print("media = %0.2f"%b)