A,B,C,D=list(map(int,input().split()))
if(B>C and D>A and C+D>A+B and C>=0 and D>=0 and A%2==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")