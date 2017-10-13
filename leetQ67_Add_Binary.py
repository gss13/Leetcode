'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
'''

def addBin(a, b):
    print '<< a = {}, b = {}'.format(a, b)
    res = []
    i = len(a) - 1
    j = len(b) - 1
    c = 0
    while (i >= 0 or j >= 0 or c != 0):
        x = int(a[i]) if i >= 0 else 0
        y = int(a[j]) if j >= 0 else 0
        temp = x + y + c
        res.append(str(temp % 2))
        c = temp//2
        i -= 1
        j -= 1
    s = ''.join(res[::-1])
    print '>> sum = {}'.format(s)
    return s

if __name__ == '__main__':
    a = '11'
    b = '1'
    addBin(a, b)
