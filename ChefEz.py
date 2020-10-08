'''input
2 
6 5 
10 5 5 3 2 1 
1 1
100
'''
try :
	t = int(input())

	for i in range(t):
		n,k = map(int, input().strip().split())
		l = list(map(int, input().strip().split()))
		carry = 0
		count = 0 
		flag = 0
		for i in range(n):
			q = carry+l[i]		# holds the number of current queries		

			if q < k:			#if current q < k, then print count
				flag = 1
				print(count+1)
				break
			count+=1
			carry = q - k		# current q - k

		if carry != 0 and flag == 0:	
			print(count+carry//k + 1)

except : pass




