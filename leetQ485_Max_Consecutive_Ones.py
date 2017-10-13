'''
Leetcode: Q485 - Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

def maxContineousOnes(arr):
	m = 0 # max number of consecutive ones
	c = 0 # running counter on consecutive ones
	for x in arr:
		if (x == 1):
			c += 1
			m = max(m, c)
		else:
			c = 0
	return m


if __name__ == '__main__':
	arr = [1, 1, 0, 1, 1, 1]
	arr = []
	arr = [0, 0, 0, 1, 0, 0, 0]
	arr = [1, 1, 1, 1, 1, 1]
	arr = [0, 0, 0, 0, 0, 0]
	arr = [0, 0, 0, 0, 0, 1]
	arr = [1, 0, 0, 0, 0, 0]
	arr = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
	#arr = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0]
	m = maxContineousOnes(arr)
	print 'Max Consecutive Ones = {}'.format(m)
