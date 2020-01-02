def isjolly(n):
	for i in range(len(n)-1):
		if 1 > abs(n[i]-n[i+1]) or abs(n[i]-n[i+1]) > len(n) - 1:
			print('no')
			return
	print('yes')

isjolly([1,4,2,3])
