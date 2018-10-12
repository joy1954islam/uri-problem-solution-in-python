linha = int(input())
n= input()
s= 0
for i in range(12):
    for j in range(12):
        v = float(input())
        if (i == linha):
            s += v

if (n == 'S'):
    print("%.1f" % s)
else:
    print("%.1f" % (s / 12.0))