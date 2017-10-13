'''
628. Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''

#Method-1: Sort the array
def max_product_sort(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

#Method-2: Find min and max numbers 
#Find out the three largest numbers and the two smallest numbers using one pass. 
def max_product_find(nums):
    #If sorted, the nums will look like: [min1, min2,......,max3, max2, max1]
    min1 = float('inf')
    min2 = float('inf')
    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')
    for n in nums:
        if n > max1:
            max3 = max2
            max2 = max1
            max1 = n
        elif n > max2:
            max3 = max2
            max2 = n
        elif n > max3:
            max3 = n
        
        if n < min1:
            min2 = min1
            min1 = n
        elif n < min2:
            min2 = n
    return max(max1*max2*max3, min1*min2*max1)
          


if __name__ == '__main__':
    nums = [6, 0, -1, -8, 1, 2]
    print max_product_sort(nums)
    print max_product_find(nums)
