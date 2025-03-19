""" "
This is a practice file for the medium problems in the LeetCode.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solutions2:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
        """
        # uses the property of a binary search tree to find the lowest common ancestor
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root

    def maxSubArray(self, nums) -> int:
        """
        Given an integer array nums, find the contiguous subarray with the largest sum and return the sum.
        """
        # uses Kadane's algorithm to find the maximum subarray sum
        max_sum = current_sum = nums[0]
        for num in nums[1:]:  # start from the second element
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

    def insertInterval(self, intervals, newInterval):
        """
        Given a list of non-overlapping intervals sorted by their start time, insert a new interval into the intervals (merge if necessary).
        """
        # uses a greedy approach to merge overlapping intervals
        result = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
            i += 1
        result.append(newInterval)
        result.extend(intervals[i:])
        return result
