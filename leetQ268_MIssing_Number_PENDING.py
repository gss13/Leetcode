'''
268. Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find 
the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it 
using only constant extra space complexity?
'''


#Solution-1: 
'''
Time: O(n)
Space: Constant

Pros:
Linear solution with constant space

Cons:
Possibility of overflow
'''
def missing_num_add(arr):
    n = len(arr)
    expected_sum = n*(n+1)/2
    actual_sum = 0
    for x in arr:
        actual_sum += x
    print 'missing number = {}'.format(expected_sum-actual_sum)


#Solution-2:
'''
Time: O(n)
Space: Constant

Pros:
Linear solution with constant space

'''
def missing_num_xor(arr):
    n = len(arr)
    res = n = len(arr)
    for i in range(n):
        res ^= i
        res ^= arr[i]
    print 'missing number = {}'.format(res)


#Solution-3:
'''
Time: O(nlogn)
Space: Constant

This solution is best when the array is already sorted.

Pros:


Cons:
Sorting takes O(nlogn)
'''    
#FIXME: This solution is not working. Fix it
def missing_num_sorted(arr):
    arr.sort()
    print arr
    start = 0
    end   = len(arr) - 1
    while (start <= end):
        mid = (start + end)//2
        if arr[mid] > mid:
            end = mid
        else:
            start = mid + 1

    print 'missing number = {}'.format(start)

if __name__ == '__main__':
    arr1 = [1, 2, 0, 4, 5]
    arr2 = [3, 1, 2, 4, 5]
    arr3 = [1, 0, 2, 3, 4]
    arrays = [arr1, arr2, arr3]
    for arr in arrays:
        print arr
        #missing_num_add(arr)
        #missing_num_xor(arr)
        missing_num_sorted(arr)
