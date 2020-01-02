def to_base(a,b):  #10進位轉不同進制(10以內)
    s=''
    while a > 0:
        s = str(a % b) + s
        a //= b
    return s

print(to_base(1000,3))

def from_base(a,b): #不同進制轉10進制(10以內)
    n = 0
    for i in range(len(a)):
        n *= b
        n += int(a[i])
        print(n)
    return n
print(from_base('1234',8))

import string  
def from_base36(a,b):  #不同進制轉10進制(含10以上)
    code = string.digits + string.ascii_uppercase
    n = 0
    for i in range(len(a)):
        n *= b
        n += code.index(a[i])
    return n 
print(from_base36('IPHONE',512))

def to_base36(a,b):    #10進制轉不同進制(含10以上)
    code = string.digits + string.ascii_uppercase
    s = ''
    while a > 0:
        s = code[a % b] + s
        a //= b
    return s
    
print(to_base36(635038972521998,512))
