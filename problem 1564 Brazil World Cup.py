while(True):
    try:
        n = int(input())
        if(n==0):
            print("vai ter copa!")
        elif(n>0):
            print("vai ter duas!")
    except EOFError:
        break