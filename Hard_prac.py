""" "
This is a practice file for the hard problems in the LeetCode.
"""

from typing import List

"""
There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. 
The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.

addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. 
It is guaranteed that there is no edge between the two nodes before adding this one.

int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. 
If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.
"""


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.edges = edges

    def addEdge(self, edge: List[int]) -> None:
        self.edges.append(edge)

    def shortestPath(self, node1: int, node2: int) -> int:
        import heapq

        graph = {i: [] for i in range(self.n)}
        for u, v, cost in self.edges:
            graph[u].append((v, cost))

        heap = [(0, node1)]
        dist = {i: float("inf") for i in range(self.n)}
        dist[node1] = 0

        while heap:
            d, u = heapq.heappop(heap)
            if u == node2:
                return d
            if d > dist[u]:
                continue
            for v, cost in graph[u]:
                if dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    heapq.heappush(heap, (dist[v], v))

        return -1


class Solutions3:
    def trap(self, height) -> int:  # height is an array of integers
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1,
        compute how much water it can trap after raining.
        """
        # uses two pointers to keep track of the left and right bounds
        left = 0
        right = len(height) - 1
        left_max = 0  # keeps track of the maximum height of the left side
        right_max = 0  # keeps track of the maximum height of the right side
        total = 0  # keeps track of the total amount of water trapped
        while left < right:
            if height[left] < height[right]:
                if (
                    height[left] >= left_max
                ):  # if the current height is greater than the left_max, update the left_max
                    left_max = height[left]
                else:
                    total += (
                        left_max - height[left]
                    )  # add the difference between the left_max and the current height to the total
                left += 1
            else:
                if (
                    height[right] >= right_max
                ):  # if the current height is greater than the right_max, update the right_max
                    right_max = height[right]
                else:
                    total += right_max - height[right]
                right -= 1
        return total

    def firstMissingPositive(self, nums) -> int:
        nums = [n for n in nums if n > 0]
        nums.sort()
        target = 1

        for n in nums:
            if n == target:
                target += 1
            elif n > target:
                return target
        return target

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
        return the area of the largest rectangle in the histogram.
        """
        # monotonic stack solution
        stack = []
        max_area = 0
        heights.append(0)  # append a sentinel value to the end of the heights array

        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        return max_area
