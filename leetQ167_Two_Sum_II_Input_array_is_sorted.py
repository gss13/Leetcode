
def twoSum_Sorted(arr, target):
    start = 0
    end   = len(arr) - 1
    while (start < end):
        if arr[start] + arr[end] == target:
            return [start, end]
        if arr[start] + arr[end] > target:
            end -= 1
        else:
            start += 1

if __name__ == '__main__':
    arr = [2, 3, 4, 4, 5, 8, 12, 15, 20, 21, 29]
    print arr
    for target in [31, 23, 9, 16, 8, 25, 49, 35]:
        print 'target = {}'.format(target)
        i, j = twoSum_Sorted(arr, target)
        print '{} + {} at index {} and {} = {}'.format(arr[i], arr[j], i, j, target)
