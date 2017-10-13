

def find_dup(arr):
    print arr
    slow = arr[0]
    fast = arr[arr[0]]
    while slow != fast:
        print '>> slow = {} and fast = {}'.format(slow, fast)
        slow = arr[slow]
        fast = arr[arr[fast]]
    print 'fast = slow = {}'.format(fast)
    fast = 0
    while slow != fast:
        print '<< slow = {} and fast = {}'.format(slow, fast)
        slow = arr[slow]
        fast = arr[fast]
    print 'Duplicate = {}'.format(slow)
    return slow

if __name__ == '__main__':
    arr = [1,2,4,3,5,4,7,6]
    find_dup(arr)

