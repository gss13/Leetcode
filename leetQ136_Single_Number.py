#Practice date: 02-May-2017

#Method-1: Using XOR
#Space Complexity: O(1)
#Time Complexity: O(n)
def singleNum_XOR(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        res ^= arr[i]
    print 'single number = {}'.format(res)


#Method-2: Using set
def singleNum_Set(arr):
    res = set()
    for n in arr:
        if n in res:
            res.remove(n)
        else:
            res.add(n)
    print res.pop()

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 1, 2, 4, 5]
    singleNum_XOR(arr)
    print '-'*20
    singleNum_Set(arr)

