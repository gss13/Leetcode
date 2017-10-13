'''
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to 
you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, 
otherwise return -1.

You may assume no duplicate exists in the array.

# Assumption: All array elements are positive integers and no repeated elements
'''

def search(arr, target):
    if not arr:
        return -l
    
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high)//2
        if (arr[mid] == target):
            return mid
        elif (arr[low] <= arr[mid]):
            if (arr[low] <= target <= arr[mid]):
                high = mid - 1
            else:
                low = mid + 1
        else:
            if (arr[mid] <= target <= arr[high]):
                low = mid + 1
            else:
                high = mid - 1
    return -1
       
        
if __name__ == '__main__':
    #arr = [4, 5, 6, 1, 2, 3]
    arr = [5, 6, 7, 1, 2, 3, 4]
    #arr = [1, 3] 
    print arr
    for target in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print 'Index of {} = {}'.format(target, search(arr, target))
