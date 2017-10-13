'''
91. Decode Ways:
A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

def decode(s):
    n = len(s)
    if n == 0:
        return n
    if n == 1:
        return 1 if s[0] > '0' else 0 
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 if s[0] > '0' else 0
    for i in xrange(2, len(dp)):
        if s[i-1] > '0':
            dp[i] += dp[i-1]
        if '10' <= s[i-2:i] < '27':
            dp[i] += dp[i-2]
    print 'No. of ways to decode "{}" = {}'.format(s, dp[len(s)])
    return dp[len(s)]
    

if __name__ == '__main__':
    s = '1223'
    decode(s)


