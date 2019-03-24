# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def quicksort(self, intervals, il, ir):
        if il >= ir:
            return intervals
        ran = int(random.uniform(il, ir))
        intervals[il], intervals[ran] = intervals[ran], intervals[il]
        temp = intervals[il].start
        i, j = il, ir
        while True:
            i += 1
            while intervals[i].start <= temp and i < ir:
                i += 1
            while intervals[j].start > temp:
                j -= 1
            if i >= j:
                break
            intervals[i], intervals[j] = intervals[j], intervals[i]

        intervals[il], intervals[j] = intervals[j], intervals[il]
        self.quicksort(intervals, il, j - 1)
        self.quicksort(intervals, j + 1, ir)
        return intervals

    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if intervals is None or intervals == []:
            return []
        # sort intervals
        # intervals.sort(key=lambda x: x.start)
        self.quicksort(intervals, 0, len(intervals) - 1)
        # merge
        rtn = []
        for i in range(len(intervals) - 1):
            if intervals[i].end >= intervals[i + 1].start:
                intervals[i + 1].start = intervals[i].start
                intervals[i + 1].end = max(intervals[i].end,
                                           intervals[i + 1].end)
            else:
                rtn.append(intervals[i])
        rtn.append(intervals[-1])
        return rtn