'''
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 --> 2
[1,3,5,6], 2 --> 1
[1,3,5,6], 7 --> 4
[1,3,5,6], 0 --> 0
'''

def findIndex(arr, val):
	'''Corner Case: If array is empty'''
	if arr is None:
		return (False, 0)

	'''Corner Case: If target is greater than last element'''
	if (arr[-1] < val):
		return (False, len(arr))

	'''Corner Case: If target is smaller than first element'''
	if(arr[0] > val):
		return (False, 0)

	low = 0
	high = len(arr) - 1
	while(low <= high):
		mid = (low + high)//2
		if (arr[mid] == val):
			return (True, mid)
		elif(arr[mid] > val):
			high = mid - 1
		else:
			low = mid + 1
	return (False, low)


if __name__ == '__main__':
	#arr = [10, 13, 14, 19, 21]
	#val = 22
	arr = [10, 13, 14, 19, 21, 25]
	val = 26
	x = findIndex(arr, val)
	if x[0]:
		print 'Found element {} at index {}'.format(val, x[1])
	else:
		print 'Element {} not found. Potential index = {}'.format(val, x[1])
