n = int(input())
for i in range(n):
    a,b = list(map(int, input().split()))
    d = 0
    if(a==b):
        print(0)
    else:
        c = 0
        if (a > b):
            c = a
            a = b
            b = c
        while (a < ( b- 1)):
            a += 1
            if(a % 2 != 0):
                d+= a
        print(d)