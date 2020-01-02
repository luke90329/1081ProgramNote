def isFullhouse(a):
    b = [x[1:] for x in a]
    s = list(set(x for x in b))
    if len(s) == 2 and b.count(s[0]) == 3 or b.count(s[0]) == 2:
        print('yes')
    else:  
        print('no')
a = [x for x in input().split(" ")]
isFullhouse(a)