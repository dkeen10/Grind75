# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

import operator


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Reverse Polish Notation Calculator.
        
        If token is a number, push onto stack.
        if token is an operator, check if lower in precedence than the top operator in the operator stack.  if yes, perform the operation.

        """
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

        stack = []

        for token in tokens:
            if token in operators:
                y, x = stack.pop(), stack.pop()
                z = operators[token](x, y)
            else:
                z = int(token)
            stack.append(z)
        return stack.pop()


    def evalRPN_v2(self, tokens: list[str]) -> int:
        """
        Reverse Polish Notation Calculator.
        
        If token is a number, push onto stack.
        if token is an operator, check if lower in precedence than the top operator in the operator stack.  if yes, perform the operation.

        """
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                y, x = stack.pop(), stack.pop()
                stack.append(x - y)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                y, x = stack.pop(), stack.pop()
                stack.append(int(x / y))
            else:
                stack.append(int(token))

        return stack.pop()

def main():
    tokens = ["2","1","+","3","*"]
    print(Solution().evalRPN(tokens))


if __name__ == "__main__":
    main()
