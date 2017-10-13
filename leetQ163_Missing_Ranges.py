
def missing_range(nums, lower, upper):
    print nums, lower, upper
    res = []
    if not nums:
        s = `lower` + '->' + `upper` if (upper-lower > 0) else `lower`
        res.append(s)
        print res
        print '\n'
        return
    exp = lower
    for acc in nums:
        if exp != acc:
            s = `exp` + '->' + `acc-1` if (acc - exp > 1) else `exp`
            res.append(s)
        exp = acc + 1
    if acc != upper:
        s = `acc+1` + '->' + `upper` if (upper - acc > 1) else `upper`
        res.append(s)
    print res
    print '\n'


if __name__ == '__main__':
    nums = [-1]
    lower = -1
    upper = 0
    missing_range(nums, lower, upper)

    nums = []
    lower = 1
    upper = 1
    missing_range(nums, lower, upper)

    nums = []
    lower = 1
    upper = 2
    missing_range(nums, lower, upper)

    nums = []
    lower = 1
    upper = 10
    missing_range(nums, lower, upper)    

    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    missing_range(nums, lower, upper)

    nums = [4, 8, 9, 50, 75, 99]
    lower = 0
    upper = 99
    missing_range(nums, lower, upper)
    

    nums = [5, 6, 9, 55, 80]
    lower = 0
    upper = 99
    missing_range(nums, lower, upper)

    nums = [9]
    lower = 0
    upper = 99
    missing_range(nums, lower, upper)    

    nums = [9]
    lower = 0
    upper = 9
    missing_range(nums, lower, upper)

    nums = [1]
    lower = 1
    upper = 9
    missing_range(nums, lower, upper)




















'''
Given a sorted interger array where the range of elements are 
in the inclusive range [lower, upper], return it's missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
return ["2", "4->49", "51->74", "76->99"]
'''




