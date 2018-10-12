while(True):
    b = 0
    sum = 0
    x=int(input())
    if(x==0):
        break
    if(x%2!=0):
        x+=1
    for a in range(5):
        sum=sum+x
        x=x+2
    print(sum)