n=int(input())
C=0
R=0
S=0
for i in range(n):
    a,ch=list(map(str,input().split()))
    a=int(a)
    if(ch == 'C'):
        C += a
    elif (ch == 'R'):
        R += a
    else:
        S += a
total=C+R+S
x=(C*100.00)/total
y=(R*100.00)/total
z=(S*100.00)/total
print("Total: {} cobaias".format(total))
print("Total de coelhos:",C)
print("Total de ratos:",R)
print("Total de sapos:",S)
print("Percentual de coelhos: %.2lf %%"%x)
print("Percentual de ratos: %.2lf %%"%y)
print("Percentual de sapos: %.2lf %%"%z)