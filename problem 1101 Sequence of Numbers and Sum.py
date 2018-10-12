while(True):
    try:
        a,b=list(map(int,input().split()))
        x = min(a,b)
        y = max(a,b)
        if(a<=0 or b<=0):
            break
        else:
            sum=0
            result = ''
            for i in range(x,y+1):
                result += str(i)+' '
                sum = sum + i
            result+= 'Sum=%d'
            print(result %sum)
    except EOFError:
        break