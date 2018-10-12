a = []
for i in range(20):    
    valor = int(input())
    a.append(valor)
pos = 0
for l in a[::-1]:
    print("N[%d] = %d" %(pos,l))
    pos += 1