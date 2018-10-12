n1 = int(input())
n2 = int(input())
t = n1
s = 0
if(n1 > n2):
    n1 = n2
    n2 = t
while(n1 <= n2):
    if(n1%13 != 0):
        s += n1
    n1 += 1
print(s)