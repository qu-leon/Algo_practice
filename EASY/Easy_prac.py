""""
This is a practice file for the easy problems in the LeetCode.
"""
class Solutions:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        """
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
        return None

    
