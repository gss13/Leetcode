'''
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

def moveZeros(nums):
    print '<< = {}'.format(nums)
    s = 0
    while s < len(nums) and nums[s] != 0:
        s += 1
    for i in xrange(s+1, len(nums)):
        if nums[i] != 0:
            nums[s], nums[i] = nums[i], nums[s]
            s += 1
    print '>> = {}\n'.format(nums) 
    
if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    moveZeros(nums)
   
    nums = [0, 0, 0, 1, 0, 0, 0, 2, 0]
    moveZeros(nums)
   
    nums = [1, 2, 3, 0, 0, 0, 4, 0, 0, 5]
    moveZeros(nums)

    nums = [0]
    moveZeros(nums)
   
    nums = [1, 2, 3, 4, 5]
    moveZeros(nums)

