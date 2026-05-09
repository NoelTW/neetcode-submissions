"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        start_times = sorted(interval.start for interval in intervals)
        end_times = sorted(interval.end for interval in intervals)
        ans = 0
        e = 0
        for s in start_times:
            if s < end_times[e]:
               ans += 1
            else:
                e += 1
        return ans 