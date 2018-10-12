c = int(input())
op = input()
s = 0

for i in range(144):
	v = float(input())
	if (i ==  c):
		s += v
		c += 12
if(op == 'S'):
	print('%.1f' %s)
else:
	print('%.1f' %(s/12.0))