#Practice date: 30-Apr-2017

def merge_sorted(arr1, arr2, m, n):
    k = m + n - 1
    m -= 1
    n -= 1
    print 'arr1 = ', arr1
    print 'arr2 = ', arr2
    while (n >=0):
        if m>= 0 and arr1[m] > arr2[n]:
            arr1[k] = arr1[m]
            m -= 1
        else:
            arr1[k] = arr2[n]
            n -= 1
        k -= 1
    print 'new_arr1 = ', arr1
           

if __name__ == '__main__':
    arr1 = [2, 3, None]
    arr2 = [1]
    m = 2
    n = 1
    merge_sorted(arr1, arr2, m, n)
    
