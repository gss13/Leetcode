'''
448. Find All Numbers Disappeared in an Array

Given an array of intergers where 1 <= a[i] <= n (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the 
returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

def findDisappearedNumbers(nums):
    for i in xrange(len(nums)):
        idx = abs(nums[i]) - 1
        nums[idx] = -1 * abs(nums[idx])
    return [i+1 for i in xrange(len(nums)) if nums[i] > 0]

if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print findDisappearedNumbers(nums)

