while(True):
    try:
        a,b=list(map(int,input().split()))
        print(abs(a-b))
    except EOFError:
        break