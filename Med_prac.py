""" "
This is a practice file for the medium problems in the LeetCode.
"""

import heapq


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
        if not nums:
            return 0

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

    def updateMatrix(self, mat):
        """
        Given a m x n binary matrix mat, return the distance of the nearest 0 for each cell.
        """
        # uses a breadth-first search approach to find the distance of the nearest 0
        m, n = len(mat), len(mat[0]) if mat else 0
        queue = []  # queue to store the indices of cells with 0
        for i in range(m):  # iterate through the matrix to find cells with 0
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float("inf")
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            i, j = queue.pop(0)
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < m and 0 <= nj < n and mat[ni][nj] > mat[i][j] + 1
                ):  # update the distance if it is shorter
                    mat[ni][nj] = mat[i][j] + 1
                    queue.append((ni, nj))
        return mat

    def kClosest(self, points, k: int):
        """
        Given an array of points in the plane and an integer k, return the k closest points to the origin (0, 0).
        """
        # uses a heap to find the k closest points
        return heapq.nsmallest(
            k, points, lambda x: x[0] ** 2 + x[1] ** 2
        )  # returns the k smallest elements from the points list based on the distance from the origin

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without duplicate characters.
        """
        # uses a sliding window approach to find the longest substring without duplicate characters
        start = 0
        max_length = 0
        char_index = {}
        for i, char in enumerate(s):
            if (
                char in char_index and char_index[char] >= start
            ):  # if the character is already in the window
                start = (
                    char_index[char] + 1
                )  # move the start of the window to the next character
                char_index[char] = i
            else:
                char_index[char] = i
                max_length = max(max_length, i - start + 1)  # update the maximum length
        return max_length

    def threeSum(self, nums):
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k] such that i != j, i != k, and j != k,
        and nums[i] + nums[j] + nums[k] == 0.
        """
        # uses a two-pointer approach to find all unique triplets that sum to zero
        nums.sort()
        result = []
        for i in range(
            len(nums) - 2
        ):  # iterate through the array 0 to n-2 to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1  # set the left and right pointers
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while (
                        left < right and nums[left] == nums[left + 1]
                    ):  # skip duplicates
                        left += 1
                    while (
                        left < right and nums[right] == nums[right - 1]
                    ):  # skip duplicates
                        right -= 1
                    left += 1
                    right -= 1
        return result

    def levelOrder(self, root: TreeNode):
        """
        Given a binary tree, return the level order traversal of its nodes' values.
        """
        # uses a breadth-first search approach to traverse the tree level by level
        if not root:  # if the tree is empty
            return []
        result = []
        queue = [root]
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    def cloneGraph(self, node: "Node") -> "Node":
        """
        Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
        """
        # uses a depth-first search approach to clone the graph
        if not node:
            return None
        visited = {}
        return self.clone(node, visited)

    def clone(self, node, visited):
        if node in visited:
            return visited[node]
        clone_node = Node(node.val, [])
        visited[node] = clone_node
        for neighbor in node.neighbors:
            clone_node.neighbors.append(self.clone(neighbor, visited))
        return clone_node

    def sortColors(self, nums) -> None:
        """
        Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same
        color are adjacent, with the colors in the order red, white, and blue.
        """
        # uses a two-pass approach to sort the colors
        red = white = 0
        blue = len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

    def productExceptSelf(self, nums):
        """
        Given an integer array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
        Solve it without division and in O(n) time complexity.
        """
        # uses two arrays to store the product of all elements to the left and right of the current element
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):  # iterate backwards
            right[i] = right[i + 1] * nums[i + 1]
        return [left[i] * right[i] for i in range(n)]

    def generateParentheses(self, n: int):
        """
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        """

        # uses a recursive approach to generate all combinations of well-formed parentheses
        result = []
        self.generate("", n, n, result)
        return result

    def generate(self, s, left, right, result):
        if left == 0 and right == 0:
            result.append(s)
            return
        if left > 0:
            self.generate(s + "(", left - 1, right, result)
        if right > left:
            self.generate(s + ")", left, right - 1, result)

    def isValidBST(self, root) -> bool:
        """
        Given the root of binary tree, determine if it is a valid BST.
        """

        # helper function with base case - recursively returns node values until it reaches the end
        def inorderTraversal(node):
            if not node:
                return []
            return (
                inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)
            )

        inorder = inorderTraversal(root)
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i - 1]:
                return False
        return True

    def canPartition(self, nums) -> bool:
        """
        Given an integer array, return Ture if you can partition the array into two subsets such that the sum of the elements
        in both subsets is equal or false otherwise.
        """
        # uses dynamic programming concept
        total = sum(nums)
        if total % 2 == 1:  # if sum of all values is odd, return false
            return False

        target = (
            total // 2
        )  # determine what is sum in which both subsets should add up to
        dp = [False] * (target + 1)
        dp[0] = True  # base case - single value will always be true

        for n in nums:
            for i in range(len(dp) - 1, n - 1, -1):
                if dp[i]:
                    continue
                if dp[i - n]:
                    dp[i] = True
                if dp[-1]:
                    return True
        return False

    def spiralOrder(self, matrix):
        """
        Given a matrix, return all elements of the matrix in spiral order.
        """
        result = []
        if not matrix or not matrix[0]:
            return result
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result
