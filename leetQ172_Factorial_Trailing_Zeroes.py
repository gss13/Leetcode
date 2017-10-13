

def leading_zeros(num):
    n = num
    zeros = 0
    while (num > 0):
        num = num/5
        zeros += num
    print 'Leading zeros in factorial of {} = {}'.format(n, zeros)

if __name__ == '__main__':
    for num in [5, 10, 20, 50, 125, 500]:
        leading_zeros(num)
        
