'''
56. Merge Intervals:
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

def mergeOverlapping(intervals):
    res = []
    intervals.sort(key=lambda x: x[0])
    s = 0
    

if __name__ == '__main__':
    intervals = [[2,6], [1,3], [15,18], [8,10]]
    mergeOverlapping(intervals)
