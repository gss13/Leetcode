#Pratice date: 30-Apr-2017

class Solution_Recursive(object):
    def rsearch(self, arr, target):
        if not arr:
            return -1
        start = 0
        end   = len(arr) - 1
        def search(arr, start, end):
            if (start > end):
                return -1
            mid = (start + end)//2
            if arr[mid] == target:
                return mid
            if arr[mid] > arr[start]:
                #Left subarry is sorted
                if arr[start] <= target < arr[mid]:
                    #Target in sorted left subarray range
                    return search(arr, start, mid-1)
                return search(arr, mid+1, end)
            else:
                #Right subarray is sorted
                if arr[mid] < target <= arr[end]:
                    #Target in sorted right subarray range
                    return search(arr, mid+1, end)
                return search(arr, start, mid-1)
        return search(arr, start, end)


    def isearch(self, arr, target):
        if not arr:
            return -1
        start = 0
        end = len(arr) - 1
        while (start <= end):
            mid = (start + end)//2
            if arr[mid] == target:
                return mid
            if arr[mid] > arr[start]:
                if arr[start] <= target < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if arr[mid] < target <= arr[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


if __name__ == '__main__':
    arr = [4, 5, 6, 7, 1, 2, 3]
    print 'Recursive Search:'
    for target in range(9):
        s = Solution_Recursive()
        index = s.rsearch(arr, target)
        if index != -1:
            print 'target {} is found at index {}'.format(target, index)
        else:
            print 'target {} is NOT found'.format(target)

    print '\n Iterative Search:'
    for target in range(9):
        index = s.isearch(arr, target)
        if index != -1:
            print 'target {} is found at index {}'.format(target, index)
        else:
            print 'target {} is NOT found'.format(target)        
