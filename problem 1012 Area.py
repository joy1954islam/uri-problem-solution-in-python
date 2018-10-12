a,b,c = list(map(float,input().split()))
triangle=0.5*a*c
circle=3.14159*c*c
trapezium=(a+b)/2.0*c
square=b*b
rectangle=a*b
print("TRIANGULO: %.3lf"%triangle)
print("CIRCULO: %.3f"%circle)
print("TRAPEZIO: %.3f"%trapezium)
print("QUADRADO: %.3f"%square)
print("RETANGULO: %.3f"%rectangle)