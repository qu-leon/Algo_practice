"""
This is a practice file for the easy problems in the LeetCode.
"""

from collections import deque
from typing import List


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
        hashmap = {}  # val: index
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

    def isHappy(self, n: int) -> bool:
        """
        Write an algorithm to determine if a number is a "happy" number.
        A happy number is a number defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits,
        and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Return true if the number is a happy number, and false otherwise.
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1

    def canPlaceFlower(self, flowerbed: List[int], n: int) -> bool:
        """
        Given a flowerbed (represented as a list of 0s and 1s) and a number n,
        return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
        """
        count = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                emptyLeft = (i == 0) or (flowerbed[i - 1] == 0)
                emptyRight = (i == length - 1) or (flowerbed[i + 1] == 0)
                if emptyLeft and emptyRight:
                    flowerbed[i] = 1
                    count += 1
        return count >= n

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

    def isBadVersion(self, n) -> bool:
        pass

    def firstBadVersion(self, n: int) -> int:
        """
        Given a number n, return the first bad version.
        """
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
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

    def climbStairs(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        """
        if n == 1:
            return 1
        one_step = 1
        two_step = 2
        for _ in range(3, n + 1):
            one_step, two_step = two_step, one_step + two_step
        return two_step

    def containsDuplicates(self, nums) -> bool:
        # brute force solution
        # num = len(nums)
        # for i in range(num):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:  # if any two elements are the same, return true
        #             return True
        # return False  # if no duplicates are found, return false

        # hash solution
        hash_set = set()
        for i in nums:
            if i in hash_set:  # if set contains current element, return True
                return True
            else:
                hash_set.add(i)  # add current element to list
        return False

    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums.extend(nums)
        return ans

    def shuffle(self, nums: list[int], n: int) -> list[int]:
        """
        Given array nums consisting of 2n elements. Return array in form of [x1, y1, x2, y2...]
        """
        ans = []
        for i, j in zip(nums[:n], nums[n:]):
            ans.append(i)
            ans.append(j)

        return ans

    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """ "
        Given a binary array nums, return the maximum number of consecutive 1's in the array.
        """
        count = 0
        count1 = 0
        for i, num in enumerate(nums):
            if num[i] == 1:
                count += 1
            else:
                count = 0
            count1 = max(count, count1)

        return count1

    def findErrorNums(self, nums: list[int]) -> list[int]:
        """
        You have a set of integers s, which originally contains all the numbers from 1 to n.
        Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
        find the number that occurs twice and the number that is missing and return them in the form of an array.
        """
        n = len(nums)
        num_set = set()
        duplicate = -1
        for num in nums:
            if num in num_set:
                duplicate = num
            else:
                num_set.add(num)
        missing = -1
        for i in range(1, n + 1):
            if i not in num_set:
                missing = i
                break
        return [duplicate, missing]

    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        """
        Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
        That is for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
        """
        result = []
        for i, num in enumerate(nums):
            count = 0
            for j, n in enumerate(nums):
                if n < num:
                    count += 1
            result.append(count)
        return result

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        Given an array nums of n integers where nums[i] is in the range [1, n],
        return an array of all integers in the range [1, n] that do not appear in nums.
        """
        num_set = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i not in num_set:
                result.append(i)
        return result

    def finalPrices(self, prices: list[int]) -> list[int]:
        """
        Given the array prices where prices[i] is the price of the ith item in a shop.
        There is a special discount for items in the shop, if you buy the ith item,
        you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i].
        If there is no such j, you will not receive any discount at all.
        Return an array where the ith element is the final price you will pay for the ith item
        """
        # brute force solution
        # result = []
        # n = len(prices)
        # for i in range(n):
        #     discount = 0
        #     for j in range(i + 1, n):
        #         if prices[j] <= prices[i]:
        #             discount = prices[j]
        #             break
        #     result.append(prices[i] - discount)
        # return result

        # monotonic stack solution
        result = prices.copy()
        stack = deque()
        for i, prices in enumerate(prices):
            while stack and prices[stack[-1]] >= prices[i]:
                result[stack.pop()] -= prices[i]
            stack.append(i)
        return result


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
