# https://leetcode.com/problems/min-stack/description/

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""


class MinStack:
    def __init__(self):
        """
        Initializes the stack object.
        
        Includes minStack to keep track of the minimum element in the stack so we can have O(1) time complexity for getMin() method.
        """
        self.stack = []        
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1],val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
    
def main():
    val  = 5
    obj = MinStack()
    obj.push(val)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()