# 78. Subsets - https://leetcode.com/problems/subsets/description/


# Given an integer array nums of unique elements, return all possible
# subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
# Constraints:
#     1 <= nums.length <= 10
#     -10 <= nums[i] <= 10
#     All the numbers of nums are unique.


#                                      [1,2,3]
#               1/                        2|         3\
#        [1],remain[2,3]             [2],remain[3]  [3],remain[]
#      2/            3\                   3|
#  [1,2],remain[3]  [1,3],remain[]   [2,3],remain[]
#      3|
#  [1,2,3],remain[]

# 1. prevent replication like [1,2] and [2,1]: use start index in backtracking
# 2. different from combination and splitting: each node has the result, not just the leaves.

# 3. termination can be skipped. If the condition `start index >= len(nums)` is met,
# the for loop is never executed, then just reaching to the bottom line which is still `return`

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(path, start_index):
            results.append(path.copy()) # each time in backtrack, add the result
            # if start_index >= len(nums):
            #     return
            for i in range(start_index, len(nums)):
                path.append(nums[i]) # get single element
                backtrack(path, i+1)
                path.pop()
        backtrack([], 0)
        return results