"""
This is a practice file for the easy problems in the LeetCode.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"


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

    def mergeTwoLists(self, list1, list2):
        """
        Merge two sorted linked lists and return it as a new sorted list.
        The new list should be made by splicing together the nodes of the first two lists.
        """
        # create a dummy node to store the head of the new list
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummy.next

    def maxProfit(self, prices) -> int:
        """
        Given an array prices where prices[i] is the price of a given stock on the ith day.
        Maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
        """
        # uses a greedy approach to find the maximum profit
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if p < buy_price:
                buy_price = p
            profit = max(profit, p - buy_price)

        return profit

    def isPalindrome(self, s: str) -> bool:
        """
        Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
        """
        # uses two pointers to check if string is a palindrome
        left_p = 0
        right_p = len(s) - 1
        while left_p < right_p:
            if not s[left_p].isalnum():
                left_p += 1  # skip non-alphanumeric char
                continue
            if not s[right_p].isalnum():
                right_p -= 1
                continue
            if s[left_p].lower() != s[right_p].lower():
                return False  # not a palindrome
            left_p += 1
            right_p -= 1
        return True

    def invertTree(self, root):
        """
        Invert a binary tree.
        """
        # recursively swaps the left and right node, starting from the root. Each iteration swaps the left and right node of the current node
        if not root:
            return
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(
                root.left
            )
            return root

    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        """
        # simple solution:
        # return Counter(s) == Counter(t)
        # own solution:
        # uses a hashmap to store the frequency of each character in the string
        mapping = {}
        for char in s:
            if char in mapping:
                mapping[char] += 1
            else:
                mapping[char] = 1
        for char in t:
            if char in mapping:
                mapping[char] -= 1
            else:
                return False
        for value in mapping.values():
            if value != 0:
                return False
        return True

    def binarySearch(self, nums, target: int) -> int:
        """
        Given a sorted array of integers, return the index of the target element. If the target is not found, return -1.
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  # to prevent overflow
            if nums[mid] == target:
                return mid  # target found
            elif nums[mid] < target:
                left = mid + 1  # continue searching in right half of array
            else:
                right = mid - 1  # continue searching left half of array
        return -1

    def floodFill(self, image, sr: int, sc: int, color: int):
        """
        An image is represented by a 2-D array of integers, each integer representing the pixel value of the image.
        Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor,
        "flood fill" the image.

        To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
        plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.
        Replace the color of all of the aforementioned pixels with the newColor.
        """
        if image[sr][sc] == color:
            return image
        newColor = image[sr][sc]
        if color != newColor:
            self.dfs(image, sr, sc, color, newColor)
        return image

    # uses a depth-first search to fill the pixels with the new color
    def dfs(
        self, image, r, c, color, newColor
    ):  # r, c are the row and column of the current pixel
        if (
            r < 0
            or r >= len(image)
            or c < 0
            or c >= len(image[0])
            or newColor != image[r][c]
        ):
            return
        image[r][c] = color
        self.dfs(image, r + 1, c, color, newColor)
        self.dfs(image, r - 1, c, color, newColor)
        self.dfs(image, r, c + 1, color, newColor)
        self.dfs(image, r, c - 1, color, newColor)

    def isBalancedBinary(self, root) -> bool:
        """
        Given a binary tree, determine if it is height balanced
        """

        # uses a recursive function to check if the tree is balanced
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1

    def hasCycle(self, head) -> bool:
        """
        Given a linked list, determine if it has a cycle in it.
        """
        # uses two pointers to detect a cycle in the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def firstBadVersion(self, n: int) -> int:
        """
        Given a number n, return the first bad version.
        """
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
        Each letter in magazine can only be used once in ransomNote.
        """
        hashmap = {}
        for char in magazine:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        for char in ransomNote:
            if char in hashmap and hashmap[char] > 0:
                hashmap[char] -= 1
            else:
                return False
        return True


class MyQueue:

    def __init__(self):
        """
        Initialize FIFO queue with two stacks
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.stack2 = self.stack1[::-1]  # reverses the stack

    def pop(self) -> int:
        return self.stack2.pop()  # removes the last element in the stack

    def peek(self) -> int:
        return self.stack2[-1]  # returns the last element in the stack

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        return False
