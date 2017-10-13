'''
266. Palindrome Permutation
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
'''

def canPermutePalindrome(s):
    cache = {}
    for c in s:
        cache[c] = c.get(c, 0) + 1
    odd_count = 0
    for k, v in cache.items():
        if v % 2 != 0:
            odd_count += 1
            if odd_count > 1: return False
    return True
        

if __name__ == '__main__':

