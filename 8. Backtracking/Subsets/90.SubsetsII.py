# 90. Subsets II - https://leetcode.com/problems/subsets-ii/description/
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
# Constraints:
#     1 <= nums.length <= 10
#     -10 <= nums[i] <= 10


#                                               [1,2,2]
#         /               1,idx0/               2,idx1|            2,idx2\
#       []✅            [1]✅,[2,2]              [2]✅,[2]        [2]repeat,[]
#                   2/          2\                2|
#              [1,2]✅,[2]   [1,2]repeat,[]   [2,2]✅,[]
#                   2|
#              [1,2,2]✅,[]


#                                                     [2,2,1,2]
#       /               2,idx0/                     2,idx1|            1,idx2\          2,idx3\
#     []✅            [2]✅,[212]                    [2],[12]           [1]✅,[2]             [2]
#                  2/       1|      2\                1/   2\              2|
#          [22]✅,[12]   [21]✅,[2]   [22]      [21],[2]    [22]          [12]
#          1/       2\      2|                  2|
#     [221]✅     [222]✅  [212]              [212]



# Note:
# 1. empty set is included
# 2. ignore duplicates at each layer
# 3. combinations: [1,2] is same as [2,1] - order does not matter

# Logic:
# 1. sort
# 2. backtrack: append path to result, create empty set at each choice to ignore repeated ones


from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(nums, path, start_index):
            res.append(path.copy())
            used = set()
            for i in range(start_index, len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    backtrack(nums, path + [nums[i]], i + 1)

        backtrack(nums, [], 0)
        return res
