def isFullhouse(a):
    b = [x[-1] for x in a]
    c = sum(b.count(x) for x in b)
    if c == 13:
        print('yes')
    else:
        print('no')
a = [x for x in input().split()]
isFullhouse(a)
