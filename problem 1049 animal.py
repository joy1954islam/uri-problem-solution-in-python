a=str(input())
b=str(input())
c=str(input())
if a == "vertebrado":
	if b=="ave":
		if c=="carnivoro":
			print("aguia")
		else:
			print("pomba")
	elif b=="mamifero":
		if c == "onivoro":
			print("homem")
		else:
			print("vaca")
elif a =="invertebrado":
	if b=="inseto":
		if c=="hematofago":
			print("pulga")
		else:
			print("lagarta")
	elif b=="anelideo":
		if c == "hematofago":
			print("sanguessuga")
		else:
			print("minhoca")