'''
325. Maximum Size Subarray Sum Equals k
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
'''

def maxSubArrayLen(nums, k):
    print 'Input Array = {}. k = {}'.format(nums, k)
    s = 0
    m = 0
    mp = {0:-1}
    for i in xrange(len(nums)):
        s += nums[i]
        if s not in mp:
            mp[s] = i
        t = s - k
        if t in mp:
            print '>>> s = {}, i = {}, t = {}, mp_t = {}, i_mp_t = {}'.format(s, i, t, mp[t], i-mp[t]) 
            m = max(m, i-mp[t])
    print mp
    print 'Max. Subarray length = {}'.format(m)
    return m

if __name__ == '__main__':
    nums = [1, -1, 5, -2, 3]
    k = 3
    maxSubArrayLen(nums, k)
    print '-'*50
    nums = [-2, -1, 2, 1]
    k = 1
    maxSubArrayLen(nums, k)
    
