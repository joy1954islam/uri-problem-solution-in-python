b=1
s=0
for i in range(1,40,2):
    m=i/b
    s=s+m
    b=b*2
print("%0.2f"%s)