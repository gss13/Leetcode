
def has_dup(arr):
    if not arr:
        return False
    cache = {}
    for x in arr:
        if x in cache:
            return True
        else:
            cache[x] = 1
    return False


if __name__ == '__main__':
    arr1 = [1, 2, 4, 5, 6, 7] 
    arr2 = [1, 2, 3, 2, 4, 5]
    arrays = [arr1, arr2]
    for arr in arrays:
        print arr
        res = has_dup(arr)
        if res:
            print 'Array contains duplicates'
        else:
            print 'Array DOES NOT contain duplicates'

