while(True):
    try:
        a,b=list(map(int,input().split()))
        print(a*b*2)
    except EOFError:
        break