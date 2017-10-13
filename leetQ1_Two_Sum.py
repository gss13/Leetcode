'''
Leetcode: 1. Two Sum
Given an array of integers, return indices of the two numbers such 
that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Note:
No where in the problem statement is given that the array is sorted.
So its not wise to assume the array is sorted even though the example
given is sorted.
'''

def findSumIndex(arr, s):
	if len(arr) < 2:
		return []
	cache = {}
	for i in range(len(arr)):
		target = s - arr[i]
		if target in cache:
			return [cache[target], i]
		else:
			cache[arr[i]] = i
	return []



if __name__ == '__main__':
	s = 9
	arr = [2, 7, 11, 15]
	print findSumIndex(arr, s)
