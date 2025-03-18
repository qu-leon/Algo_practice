""" "
This is a practice file for the hard problems in the LeetCode.
"""


class Solutions3:
    def trap(self, height) -> int:  # height is an array of integers
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
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
