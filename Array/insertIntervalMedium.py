# https://leetcode.com/problems/insert-interval/description/


"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        we can iterate though the intervals and change the newInterval until newInterval is insterted.
        """
        resulting_intervals = []
        i = 0

        # while the end interval in intervals is less than the beginning interval in the interval to be added, no change needed.
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            resulting_intervals.append(intervals[i])
            i += 1

        # now we are at the state where we need to merge newInterval into the existing interval array.
            
        # while the beginning interval in intervals is less than the end interval of newInterval, we update newInterval.to encompass the whole range
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        resulting_intervals.append(newInterval)
        
        # now we are at the state where newInterval has been inserted/absorbed into the interval array.

        # now we can cleanup by adding the rest of the intervals to the resulting interval array.
        while i < len(intervals):
            resulting_intervals.append(intervals[i])
            i += 1  

        return resulting_intervals  
        

def main():
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(Solution().insert(intervals, newInterval))

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(Solution().insert(intervals, newInterval))


if __name__ == "__main__":
    main()
