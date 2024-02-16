# https://aaronice.gitbook.io/lintcode/sweep-line/meeting-rooms

"""
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), 
determine if a person could attend all meetings
Ex1:
Input:
[[0,30],[5,10],[15,20]]
Output:
 false

 Ex2:
 Input:
 [[7,10],[2,4]]

Output:
 true
"""
 
 
class Solution:
    def canAttendMeetings(intervals):
        """
        Approach: check each successive interval to see if its start time comes before the previous interval's end time.
        Use Enumerate to get access to index i and value.
        Time complexity: 0(n) since we're iterating once and O(1) space complexity since we're using constant num of variables
        """
        intervals.sort(key=lambda x: x[0])
        for i, interval in enumerate(intervals):
            # since we only care about the start, we don't need to define the end
            start, _ = interval
            if i > 0 and start < intervals[i - 1][1]:
                return False
        return True
    

def main():
    intervals = [[0,30],[5,10],[15,20]]
    print(Solution.canAttendMeetings(intervals))
    
    intervals = [[7,10],[2,4]]
    print(Solution.canAttendMeetings(intervals))   


if __name__ == "__main__":
    main()
