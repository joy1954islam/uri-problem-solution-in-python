while(True):
    try:
        a,b=list(map(int,input().split()))
        if(a==b):
            break
        else:
            if(a<b):
                print("Crescente")
            else:
                print("Decrescente")
    except EOFError:
        break