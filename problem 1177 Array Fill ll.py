n=int(input())
tmp=0
for i in range(1000):
    print("N[%d] = %d" %(i,tmp))
    tmp += 1
    if (tmp == n):
        tmp = 0