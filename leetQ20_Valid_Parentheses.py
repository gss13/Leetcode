'''
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid 
but "(]" and "([)]" are not.
'''


def check_paren(string):
	cache = {'}': '{', ')': ')', ']': '['}
	stack = []
	for s in string:
		if s in '{([':
			stack.append(s)
		elif ((stack == []) or (stack.pop() != cache[s])): 
			return False
	return stack == []


if __name__ == '__main__':
	string = '{}'
	if check_paren(string):
		print 'Valid Parentheses'
	else:
		print 'Invalid Parentheses'
