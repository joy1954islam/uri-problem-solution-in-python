n = int(input())
for i in range(n):
    a,b=list(map(int,input().split()))
    if(b == 0):
        print("divisao impossivel")
    else:
        print("%.1f" %(a / b))