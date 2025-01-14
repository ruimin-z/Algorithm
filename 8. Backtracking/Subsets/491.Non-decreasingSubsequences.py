# 491. Non-decreasing Subsequences - https://leetcode.com/problems/non-decreasing-subsequences/description/
#
# Given an integer array nums, return all the different possible non-decreasing subsequences
# of the given array with at least two elements. You may return the answer in any order.
#
# Example 1:
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#
# Example 2:
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
#
# Constraints:
#     1 <= nums.length <= 15
#     -100 <= nums[i] <= 100


#                                       [4,6,3,7]
#                       4/              6|              3|      7\
#               [4],[6,3,7]           [6],[3,7]       [3],[7]    [7],[]         ----> ignore
#              6/    3|    7\          3/   7\          7|         x
#     [4,6],[3,7]    x     [4,7][]     x    [6,7][]   [3,7][]                   ----> store in results
#       3/   7\
#       x    [4,6,7]                                                            ----> store in results


#                                               [4,6,7,7]
#                           4/                     6|                7|       7\
#                     [4],[6,7,7]               [6],[7,7]          [7],[7]     [7]x      ----> ignore
#              6/          7|     7\            7/    7\             7|       repeated
#     [4,6],[7,7]       [4,7][7]  [4,7]x   [6,7][]  [6,7]x     [7,7][]                   ----> store duos in results
#       7/   7\            7|     repeated          repeated
#  [4,6,7][7] [4,6,7]x  [4,7,7][]                                                        ----> store triplets in results
#       7|    repeated
#  [4,6,7,7]                                                                             ----> store quadruplets



# 1. subsets backtracking: store results at internal and leaf nodes
# 2. repetition: repeated elements.
#                Notice that result is skipped if there are same result at each **level**.
#                Removing elements at each level is **more efficient** than at global level.
# This is DFS

from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(path, index):
            if len(path) >= 2:
                results.append(path.copy())
            found = set()     # interesting!
            for i in range(index, len(nums)):
                if nums[i] not in found and (not path or path[-1] <= nums[i]):
                    found.add(nums[i])
                    path = path + [nums[i]]
                    backtrack(path, i + 1)
                    path.pop()
                else:
                    continue

        backtrack([], 0)
        return results
