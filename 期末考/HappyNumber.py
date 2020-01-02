def f(n):
	while True:
		count = 0
		for i in str(n):
			count += int(i)**2
		n = count
		if n == 1:
			print('yes')
			break
		elif n == 4:
			print('no')
			break
