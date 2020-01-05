w = open('data.txt','r').read()
w = [x for x in w.split()]
del w[1]
if w.count(w[0]) > 1:
    print('yes')
else:
    print('no')
