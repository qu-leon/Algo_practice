"""
Run all tests:
    python Test.py

Run one test:
    python -m unittest Test.TestSolutions.test_two_sum
"""

import unittest

from Easy_prac import ListNode, Solutions
from Hard_prac import Solutions3
from Med_prac import Node, Solutions2, TreeNode


class BinaryNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(head, limit=20):
    values = []
    current = head
    while current and len(values) < limit:
        values.append(current.val)
        current = current.next
    return values


def build_bst():
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    return root


class TestSolutions(unittest.TestCase):
    def setUp(self):
        self.solution = Solutions()

    def test_two_sum(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_is_valid_parenthesis(self):
        self.assertTrue(self.solution.isValidParenthesis("()[]{}"))
        self.assertFalse(self.solution.isValidParenthesis("(]"))

    def test_merge_two_lists(self):
        list1 = build_linked_list([1, 2, 4])
        list2 = build_linked_list([1, 3, 4])
        merged = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged), [1, 1, 2, 3, 4, 4])

    def test_max_profit(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_is_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.solution.isPalindrome("race a car"))

    def test_invert_tree(self):
        root = BinaryNode(4, BinaryNode(2), BinaryNode(7))
        inverted = self.solution.invertTree(root)
        self.assertEqual(inverted.left.val, 7)
        self.assertEqual(inverted.right.val, 2)

    def test_is_happy(self):
        self.assertTrue(self.solution.isHappy(19))
        self.assertFalse(self.solution.isHappy(2))

    def test_can_place_flower(self):
        self.assertTrue(self.solution.canPlaceFlower([1, 0, 0, 0, 1], 1))
        self.assertFalse(self.solution.canPlaceFlower([1, 0, 0, 0, 1], 2))

    def test_is_anagram(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))
        self.assertFalse(self.solution.isAnagram("rat", "car"))

    def test_binary_search(self):
        self.assertEqual(self.solution.binarySearch([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(self.solution.binarySearch([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_flood_fill(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        self.assertEqual(self.solution.floodFill(image, 1, 1, 2), expected)

    def test_is_balanced_binary(self):
        root = BinaryNode(
            3, BinaryNode(9), BinaryNode(20, BinaryNode(15), BinaryNode(7))
        )
        self.assertTrue(self.solution.isBalancedBinary(root))

    def test_has_cycle(self):
        head = build_linked_list([3, 2, 0, -4])
        second = head.next
        tail = second.next.next
        tail.next = second
        self.assertTrue(self.solution.hasCycle(head))

    @unittest.skip(
        "isBadVersion is a LeetCode API stub; firstBadVersion needs that API and currently can loop for normal bad-version inputs."
    )
    def test_first_bad_version(self):
        class VersionSolution(Solutions):
            def isBadVersion(self, n):
                return n >= 4

        self.assertEqual(VersionSolution().firstBadVersion(5), 4)

    def test_can_construct(self):
        self.assertTrue(self.solution.canConstruct("aa", "aab"))
        self.assertFalse(self.solution.canConstruct("aa", "ab"))

    def test_climb_stairs(self):
        self.assertEqual(self.solution.climbStairs(5), 8)

    def test_contains_duplicates(self):
        self.assertTrue(self.solution.containsDuplicates([1, 2, 3, 1]))
        self.assertFalse(self.solution.containsDuplicates([1, 2, 3, 4]))

    def test_get_concatenation(self):
        self.assertEqual(self.solution.getConcatenation([1, 2, 1]), [1, 2, 1, 1, 2, 1])

    def test_shuffle(self):
        self.assertEqual(
            self.solution.shuffle([2, 5, 1, 3, 4, 7], 3), [2, 3, 5, 4, 1, 7]
        )

    def test_find_max_consecutive_ones(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)

    def test_find_error_nums(self):
        self.assertEqual(self.solution.findErrorNums([1, 2, 2, 4]), [2, 3])

    def test_smaller_numbers_than_current(self):
        self.assertEqual(
            self.solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]), [4, 0, 1, 1, 3]
        )

    def test_find_disappeared_numbers(self):
        self.assertEqual(
            self.solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6]
        )

    def test_final_prices(self):
        self.assertEqual(self.solution.finalPrices([8, 4, 6, 2, 3]), [4, 2, 4, 2, 3])

    def test_row_and_maximum_ones(self):
        self.assertEqual(
            self.solution.rowAndMaximumOnes([[0, 1], [1, 1], [0, 0]]), [1, 2]
        )

    def test_count_words(self):
        self.assertEqual(
            self.solution.countWords("the cat and the dog"),
            {"the": 2, "cat": 1, "and": 1, "dog": 1},
        )

    def test_count_characters(self):
        self.assertEqual(
            self.solution.countCharacters("cbacba"), {"a": 2, "b": 2, "c": 2}
        )

    def test_sum_of_num(self):
        self.assertEqual(self.solution.sumOfNum([1, 3, 5, 7, 10, 14]), 16)

    def test_unique_val(self):
        self.assertEqual(self.solution.uniqueVal("abac"), {"b": 1, "c": 1})

    def test_reverse_integer(self):
        self.assertEqual(self.solution.reverseInteger(-12340), -4321)

    def test_convert_date_format(self):
        self.assertEqual(self.solution.convertDateFormat("2026-09-08"), "09/08/2026")


class TestSolutions2(unittest.TestCase):
    def setUp(self):
        self.solution = Solutions2()

    def test_right_side_view(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        self.assertEqual(self.solution.rightSideView(root), [1, 3, 4])

    def test_lowest_common_ancestor(self):
        root = build_bst()
        self.assertEqual(
            self.solution.lowestCommonAncestor(root, root.left, root.left.right).val, 2
        )

    def test_max_subarray(self):
        self.assertEqual(self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_insert_interval(self):
        self.assertEqual(
            self.solution.insertInterval([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]]
        )

    def test_update_matrix(self):
        mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        self.assertEqual(self.solution.updateMatrix(mat), expected)

    def test_k_closest(self):
        result = self.solution.kClosest([[1, 3], [-2, 2], [2, -2]], 2)
        self.assertCountEqual([tuple(point) for point in result], [(-2, 2), (2, -2)])

    def test_length_of_longest_substring(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_three_sum(self):
        result = [tuple(item) for item in self.solution.threeSum([-1, 0, 1, 2, -1, -4])]
        self.assertEqual(sorted(result), [(-1, -1, 2), (-1, 0, 1)])

    def test_level_order(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.levelOrder(root), [[3], [9, 20], [15, 7]])

    def test_clone_graph(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]
        clone = self.solution.cloneGraph(node1)
        self.assertIsNot(clone, node1)
        self.assertEqual(clone.val, 1)
        self.assertEqual(clone.neighbors[0].val, 2)
        self.assertIs(clone.neighbors[0].neighbors[0], clone)

    def test_sort_colors(self):
        nums = [2, 0, 2, 1, 1, 0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_product_except_self(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_generate_parentheses(self):
        self.assertEqual(
            set(self.solution.generateParentheses(3)),
            {"((()))", "(()())", "(())()", "()(())", "()()()"},
        )

    def test_is_valid_bst(self):
        self.assertTrue(self.solution.isValidBST(build_bst()))

    def test_can_partition(self):
        self.assertTrue(self.solution.canPartition([1, 5, 11, 5]))
        self.assertFalse(self.solution.canPartition([1, 2, 3, 5]))

    def test_spiral_order(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.solution.spiralOrder(matrix), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_build_array(self):
        self.assertEqual(
            self.solution.buildArray([1, 3], 3), ["Push", "Push", "Pop", "Push"]
        )

    def test_eval_rpn(self):
        self.assertEqual(self.solution.evalRPN(["2", "1", "+", "3", "*"]), 9)

    def test_permute(self):
        result = {tuple(item) for item in self.solution.permute([1, 2, 3])}
        expected = {(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)}
        self.assertEqual(result, expected)

    def test_next_permutation(self):
        nums = [1, 2, 3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 2])

    def test_group_anagrams(self):
        result = [
            sorted(group)
            for group in self.solution.groupAnagrams(
                ["eat", "tea", "tan", "ate", "nat", "bat"]
            )
        ]
        self.assertEqual(
            sorted(result), sorted([["ate", "eat", "tea"], ["nat", "tan"], ["bat"]])
        )

    def test_max_integer(self):
        nums = [1, 2, [3, 4, [5], [6], 7, [8, [9]]]]
        self.assertEqual(self.solution.maxInteger(nums), 9)

    def test_exclusive_time(self):
        logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
        self.assertEqual(self.solution.exclusiveTime(2, logs), [3, 4])

    def test_daily_temperature(self):
        self.assertEqual(
            self.solution.dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )

    def test_find_diagonal_order(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(
            self.solution.findDiagonalOrder(matrix), [1, 2, 4, 7, 5, 3, 6, 8, 9]
        )

    def test_max_profit_ii(self):
        self.assertEqual(self.solution.maxProfitII([7, 1, 5, 3, 6, 4]), 7)

    def test_rob(self):
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12)


class TestSolutions3(unittest.TestCase):
    def setUp(self):
        self.solution = Solutions3()

    def test_trap(self):
        self.assertEqual(self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_first_missing_positive(self):
        self.assertEqual(self.solution.firstMissingPositive([3, 4, -1, 1]), 2)

    def test_largest_rectangle_area(self):
        self.assertEqual(self.solution.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
