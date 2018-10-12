a = float(input())
if(a>=0 and a<=400):
	b= a*0.15
	c=a+b
	d=15
elif(a>=400.01 and a<=800.00):
	b=a*0.12
	c=a+b
	d=12
elif(a>=800.01 and a<=1200.00):
    b=a*0.1
    c=a+b
    d=10
elif(a>=1200.01 and a<=2000.00):
	b=a*0.07
	c=a+b
	d=7
elif(a>2000):
	b=a*0.04
	c=a+b
	d=4
print("Novo salario: %.2f"%c)
print("Reajuste ganho: %.2f"%b)
print("Em percentual: {} {}".format(d,"%"))