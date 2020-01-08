def f(n):
	s = []
	while n != 1:
		if n % 2 == 0:
			n //= 2
		else:
			n = 3*n + 1
		s.append(n)
	print(len(s)+1) #記得加上原本的數字
num = 10
f(num)
