def f(n):
    while n != 1:
        count = 0
        for i in str(n):
            count += int(i)**2
        n = count
        if n == 4:
            print('no')
            return
    print('yes')
