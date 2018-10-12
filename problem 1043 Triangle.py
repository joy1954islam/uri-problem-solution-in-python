a,b,c=list(map(float,input().split()))
if(a<b+c and b < a + c and c < a + b):
     print("Perimetro = %0.1f"%(a + b + c))
else:
     print("Area = %0.1f"%((c * (a + b)) / 2))