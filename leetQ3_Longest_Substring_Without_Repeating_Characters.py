'''
Leetcode: Q3.Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without 
repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence 
and not a substring.

'''

def max_sub_string_len_wo_repeating(s):
	if not s:
		return 0
	seen = {}
	start = 0
	max_len = 0
	current_len = 0
	for i, c in enumerate(s):
		if c in seen and start <= seen[c]:
			start = seen[c] + 1
		else:
			current_len = i - start + 1
			max_len = max(max_len, current_len)
		seen[c] = i

	return max_len

if __name__ == '__main__':
	string = ['aab', 'pwwkew', 'bbbb', 'abcabcbb', 'dvdf', 'dvegdab', 'tmmzuxt', '']
	for s in string:
		max_len = max_sub_string_len_wo_repeating(s)
		print 'Longest sub-string lenght of "{}" w/o repeated character = {}'.format(s, max_len)


'''
Solution (Linear Time: O(n))
Let us talk about the linear time solution now. This solution uses 
extra space to store the last indexes of already visited characters. 
The idea is to scan the string from left to right, keep track of the 
maximum length Non-Repeating Character Substring (NRCS) seen so far. 
Let the maximum length be max_len. When we traverse the string, 
we also keep track of length of the current NRCS using cur_len variable. 
For every new character, we look for it in already processed part of 
the string (A temp array called visited[] is used for this purpose). 
If it is not present, then we increase the cur_len by 1. If present, 
then there are two cases:

a) The previous instance of character is not part of current NRCS 
(The NRCS which is under process). In this case, we need to simply 
increase cur_len by 1.
b) If the previous instance is part of the current NRCS, then our 
current NRCS changes. It becomes the substring staring from the next
character of previous instance to currently scanned character. 
We also need to compare cur_len and max_len, before changing current 
NRCS (or changing cur_len).

'''

