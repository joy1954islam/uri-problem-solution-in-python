new_list=[0,1]
a=0
t=1

for i in range(60):
    tnp = t+a
    new_list.append(tnp)
    a=t
    t=tnp

n = int(input())
for i in range(n):
    valor = int(input())
    print('Fib(%d) = %d' %(valor,new_list[valor]))