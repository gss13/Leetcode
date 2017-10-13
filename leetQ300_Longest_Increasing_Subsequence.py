#Practice date: 06-May-2017

#Solution-1:
#Time: O(n^2)
#Space: O(n)
def lis(arr):
    b = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j]:
                b[i] = max(b[i], b[j] +1)
    max_len = 0
    for i in range(len(b)):
        max_len = max(max_len, b[i])
    print 'Longest increasing subsequence lenght = {}'.format(max_len)



if __name__ == '__main__':
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    arr = [15, 27, 14, 38, 26, 55, 46, 65, 85]
    lis(arr)
