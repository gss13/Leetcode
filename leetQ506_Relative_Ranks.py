
def findRelativeRanks(nums):
    mapping = {}
    rank = []
    sorted_nums = sorted(nums, reverse=True)
    for i, v in enumerate(sorted_nums):
        print i, ':', v
        if i == 0:
            mapping[v] = 'Gold Medal'
        elif i == 1:
            mapping[v] = 'Silver Medal'
        elif i == 2:
            mapping[v] = 'Bronze Medal'
        else:
            mapping[v] = `i+1`
    print '>>> ', mapping
    for n in nums:
        rank.append(mapping[n])
    print rank
    

if __name__ == '__main__':
    nums = [5, 4, 3, 2, 1]
    nums = [10, 3, 8, 9, 4]
    findRelativeRanks(nums)
