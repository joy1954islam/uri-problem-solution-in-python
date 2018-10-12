n=int(input())
for i in range(n):
    a,b=list(map(int,input().split()))
    if(a%2==1):
        c=0
        for j in range(1,b+1):
            c=c+a
            a=a+2
        print(c)
    else:
        a+=1
        c=0
        for j in range(1,b+1):
            c+=a
            a+=2
        print(c)