'''
Leetcode: Q278. First Bad Version

You are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the quality 
check. Since each version is developed based on the previous version, all the 
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first 
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether 
version is bad. Implement a function to find the first bad version. You should 
minimize the number of calls to the API.
'''

def isBadVersion(version):
    if version >= 3:
        return True
    return False


def firstBadVersion(n):
    if n == 1:
        return n
    start = 1
    end = n
    while start < end:
        mid = (start + end)//2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1
    print 'First bad version = {}'.format(start)
    return start

if __name__ == '__main__':
    n = 10
    firstBadVersion(n)


