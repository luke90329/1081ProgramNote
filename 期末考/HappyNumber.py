def f(n):
    while n != 1:
        sum = 0
        for i in str(n):
            sum += int(i)**2
        n = sum
        if n == 4:
            print('no')
            return
    print('yes')
num = 10
f(num)
