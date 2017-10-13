'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways 
can you climb to the top? Given n will be a positive integer
'''

#Solution-1
def solution_1(n):
    if n < 3:
        return n
    return solution_1(n-1) + solution_1(n-2)

if __name__ == '__main__':
    n = 6
    r = solution_1(n)
    print 'n = {}, r = {}'.format(n, r)
