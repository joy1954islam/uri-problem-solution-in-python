n1,n2,n3,n4=list(map(float,input().split()))
a=(((n1*2)+(n2*3)+(n3*4)+(n4*1))/10);
print("Media: %.1lf"%a)
if(a>=7.0):
	print("Aluno aprovado.")
elif(a<5.0):
	print("Aluno reprovado.")
elif(a>=5.0 and a<=6.9):
	print("Aluno em exame.")
	n5=float(input())
	print("Nota do exame: %.1lf"%n5)
	b=(a+n5)/2
	if(b>=5.0):
		print("Aluno aprovado.")
	if (b<=4.9):
			print("Aluno reprovado.")
	print("Media final: %.1lf"%b)