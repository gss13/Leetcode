import math


def licenseKeyFormatting(S, K):
    char_count = 0
    for ch in S:
        if ch != '-':
            char_count += 1
    dash_count = int(math.ceil(char_count/float(K))) - 1
    res = [0] * (char_count + dash_count)
    d_count = 0
    c_count = 0
    j = len(res) - 1
    for i in range(len(S) - 1, -1, -1):
        print 'ch = {}, count = {}, S = {}, res = {}'.format(S[i], d_count, S, res)
        if d_count == K and char_count > c_count:
            res[j] = '-'
            j -= 1
            d_count = 0
        if S[i] != '-':
            res[j] = S[i].capitalize() if S[i].isalpha() else S[i]
            j -= 1
            d_count += 1
            c_count += 1
    print ''.join(res)


if __name__ == '__main__':
    S = '--a-a-a-a--'
    K = 2
    licenseKeyFormatting(S, K)
