n = int(input())
lista = list(map(int, input().split()))
p = 0
m = lista[0]
count = 0
for i in lista:
    if (i < m):
        m = i
        p = count
    count += 1
print("Menor valor: %d" % m)
print("Posicao: %d" % p)

