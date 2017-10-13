'''
The Hamming distance between two integers is the number of positions at 
which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)

The above arrows point to positions where the corresponding bits are different.
'''

def hammingDistance1(x, y):
    dis = 0
    print 'x = {}, y = {}'.format(x, y)
    while x or y:
        if x % 2 != y % 2: dis += 1
        x /= 2
        y /= 2
    print 'Hamming Distance = {}'.format(dis)
    return dis

if __name__ == '__main__':
    x = 3
    y = 4
    hammingDistance1(x, y)
    
    

