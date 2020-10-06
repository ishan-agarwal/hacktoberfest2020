'''input
5 6 5
23
30
42
57
90
21 
23 
35 
57 
90 
92 
21 
23 
30 
57 
90 
'''

try : 
	n = list(map(int, input().split()))
	l = []
	for i in range(len(n)):
		k = []
		for j in range(n[i]):
			t = input()
			k.append(int(t))
		l.append(k) 

	l1 = l[0]
	l2 = l[1]
	l3 = l[2]


	i1 = set(l1).intersection(l2)
	i2 = set(l2).intersection(l3)
	i3 = set(l3).intersection(l1)

	res = sorted(i1 | i2 | i3)
	print(len(res))

	for i in res: print(i)

except : pass