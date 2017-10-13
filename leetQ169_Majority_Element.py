#Practice date: 02-May-2017

#Solution-1
def majorityElement(nums):
    from collections import Counter
    count = Counter()
    for n in nums:
        count[n] += 1
    return count.most_common(1)[0][0]

#Solution-2
def majority(arr):
    cache = {}
    m = len(arr)//2 + 1
    for item in arr:
        if item in cache:
            cache[item] += 1
        else:
            cache[item] = 1
    for key, value in cache.items():
        if value >= m:
            print key

#Solution-3:
def majority_element(arr):
    maj = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if count == 0:
            count += 1
            maj = arr[i]
        elif maj == arr[i]:
            count += 1
        else:
            count -= 1
    print 'Major Element = {}'.format(maj)
        

if __name__ == '__main__':
    arr = [2, 3, 4, 2, 2, 3, 3, 3, 3]
    majorityElement(arr) # Solution-3 (Medium)
    majority(arr) # Solution-2 (Ok)
    majority_element(arr) # Solution-3 (Best)    


