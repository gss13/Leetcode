#Practice date: 29-Apr-2017

'''
Working solution
Removes dups in place and also maintains the order
'''
def remove_dup(nums):
    if not nums:
        return 0
    start = 0
    print '<<<', nums
    for i in range(1, len(nums)):
        if nums[start] != nums[i]:
            start +=1
            nums[start] = nums[i]
    print 'Length of {} = {}'.format(nums, start+1)

'''
Not complete soultion
Returns the new lenght correctly, 
but does not maintain the order of the array
'''
def remove_dup(nums):
    if not nums:
        return 0
    p = len(nums) - 1
    print '<<<', nums
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            temp = nums[p]
            nums[p] = nums[i]
            nums[i] = temp
            p -= 1
    print '>>>', nums
    print 'Length of {} = {}'.format(nums, p+1)


if __name__ == '__main__':
    nums1 = [1, 2, 4, 4, 9]
    nums2 = []
    nums3 = [0, 0, 4, 5]
    nums4 = [-1, 0, 0]
    nums5 = [1, 1, 2, 2, 3]
    nums6 = [1, 1, 2, 3]
    nums  = [nums1, nums2, nums3, nums4, nums5, nums6]
    for n in nums:
        remove_dup(n)
