#Practice date: 29-Apr-2017

def remove_element(arr, val):
    if not arr:
        return 0
    print '<<<', arr
    start = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[start] = arr[i]
            start += 1
    print '>>>', arr
    print 'Lenght of array after removing element = {}'.format(start)

if __name__ == '__main__':
    val = 3
    nums1 = [3, 3, 3, 2, 5, 7]
    nums2 = []
    nums3 = [3, 3, 3, 3]
    nums4 = [2, 4, 5, 6]
    nums5 = [5, 6, 3, 4, 3, 6, 3]
    nums  = [nums1, nums2, nums3, nums4, nums5]
    for n in nums:
        remove_element(n, val) 
