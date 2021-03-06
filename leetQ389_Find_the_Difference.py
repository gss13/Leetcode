'''
389. Find the Difference
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter 
at a random position.

Find the letter that was added in t.

Example:
Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''

#Method-1: Using XOR
def findTheDifference_xor(s, t):
    res = 0
    for ch in s:
        res ^= ord(ch)
    for ch in t:
        res ^= ord(ch)
    return chr(res)

#Method-2: Using Sets
#This method fails for string containing duplicate characters.
#Sets approch is not useful here
def findTheDifference_set(s, t):
    return (set(t) - set(s)).pop()

#Method-3: Using Dictionary
def findTheDifference_dict(s, t):
    pass


if __name__ == '__main__':
    s = 'abcd'
    t = 'abcde' 
    print findTheDifference_xor(s, t)
    s = 'a'
    t = 'aa'
    print findTheDifference_xor(s, t)
