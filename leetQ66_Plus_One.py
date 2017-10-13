'''
Given a non-nagative integer represented as a non-empty array 
of digits, plus one to the interger. You may assume the integer 
do not contain any leading zeros, except the number 0 itself.
The digits are stored such that the most significant digit is at 
the head of the list.
'''

def plus_one(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        arr[i] = 0
    arr.insert(0, 1)
    return arr

if __name__ == '__main__':
    array = [[9], [9,9], [9,9,9], [9,9,9,9], [8,9], [8,9,9], [9,8,9,9], [7,0,9,0]]
    for arr in array:
        print 'Before = {}'.format(arr)
        res = plus_one(arr)
        print 'After = {}'.format(res)
        print '-'*10
        
    
