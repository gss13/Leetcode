'''
Leet 15: 3Sum
Given an array S of n intergers, are there elements a, b, c in S such
that a+b+c=0? Find all unique triplets in the array which gives the sum
of zero.

For example, given array S = [-1, 0, 1, 2, -1, -4]
A solution set is: [[-1, 0, 1], [-1, -1, 2]]
'''

def threeSum(nums):
    nums.sort()
    print nums
    res = []
    res_idx = []
    s = set()
    for i in xrange(len(nums)):
        if i  > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        left, right = i+1, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                res.append((nums[i], nums[left], nums[right]))
                res_idx.append((i, left, right))
                s.add((nums[i], nums[left], nums[right]))
                while right > left and nums[left] == nums[left+1]: left += 1
                while right > left and nums[right] == nums[right-1]: right -= 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
    print len(res)
    for item1, item2 in zip(res, res_idx):
        print item1, '::', item2
    print '-'*10
    print list(s)


if __name__ == '__main__':
    nums = [-4, -4, -1, -1, -1, 0, 0, 1, 1, 2, 2, 5, 5]
    threeSum(nums)
    print '='*20
    nums = [-1, 0, 1, 2, -1, -4]
    threeSum(nums)
