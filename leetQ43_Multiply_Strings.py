'''
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2 (also a string).

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

def multiply(n1, n2):
    p = 0
    print '<< n1 = {}, n2 = {}'.format(n1, n2)
    print '>> product of {} and {} = {}'formata(n1, n2, p)

if __name__ == '__main__':
    n1 = '4'
    n2 = '8'
    multiply(n1, n2)

    n1 = '4'
    n2 = '12'
    multiply(n1, n2)

    n1 = '13'
    n2 = '15'
    multiply(n1, n2)

    n1 = '0'
    n2 = '8'
    multiply(n1, n2)
