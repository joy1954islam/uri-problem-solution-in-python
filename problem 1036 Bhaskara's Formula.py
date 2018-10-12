A,B,C = list(map(float,input().split()))
d = B * B - 4 * A * C
e = pow(d, .5)
if (d < 0 or A == 0):
    print("Impossivel calcular")
else:
    f = (-B + e) / (2 * A)
    g = (-B - e) / (2 * A)
    print("R1 = %.5lf"%f)
    print("R2 = %.5lf"%g)
