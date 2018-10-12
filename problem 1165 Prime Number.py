n=int(input())
for i in range(n):
    a=int(input())
    c=0
    for j in range(1,a+1):
        if(a%j==0):
            c=c+1
    if(c==2):
        print("{} eh primo".format(a))
    else:
        print("{} nao eh primo".format(a))