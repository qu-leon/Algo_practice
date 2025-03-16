""" "
This is a practice file for the easy problems in the LeetCode.
"""


class Solutions:
    def twoSum(self, nums, target: int):
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        """
        # uses a hashmap to store the difference between the target and the current number
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
        return None

    def isValidParenthesis(self, s: str) -> bool:
        """
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
        """
        # uses a stack to keep track of the open brackets
        stack = []
        # mapping of the closing brackets to the opening brackets
        mapping = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
