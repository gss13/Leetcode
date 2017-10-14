'''
Given a set of candidate numbers (C) (without duplicates) and a 
target number (T), find all unique combination in C where the 
candidate numbers sum to T

The same repeated number may be chosen from C unlimited number 
of times.

Note:
1.All numbers (including target) will be positive integers.
2.The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[[7], [2, 2, 3]]
'''

class Solution1(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        self.res = []
        self.target = target
        candidates.sort()
        self.dfs(candidates, 0, 0, [])
        return self.res
    
    def dfs(self, candidates, summ, idx, path):
        if summ == self.target:
            self.res.append(path)
            return
        for i in xrange(idx, len(candidates)):
            if summ + candidates[i] <= self.target:
                self.dfs(candidates, summ + candidates[i], i, path + [candidates[i]])
            else:
                return 

def combinationSum(candidates, target):
    if not candidates:
        return []
    res = []
    candidates.sort()
    def dfs(candidates, target, idx, path):
        if target == 0:
            res.append(path)
            return
        for i in xrange(idx, len(candidates)):
            if candidates[i] > target:
                break
            dfs(candidates, target-candidates[i], i, path + [candidates[i]])
    dfs(candidates, target, 0, [])
    return res 


if __name__ == '__main__':
    candidates = [1, 2]
    target = 4
    S = Solution1()
    print S.combinationSum(candidates, target)

    candidates = [2, 3, 6, 7]
    target = 7
    print S.combinationSum(candidates, target)
   
    candidates = [3,12,9,11,6,7,8,5,4]
    target = 15
    print S.combinationSum(candidates, target)
