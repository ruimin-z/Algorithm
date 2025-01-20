# 46. Permutation - https://leetcode.com/problems/permutations/description/
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#
# Example 3:
# Input: nums = [1]
# Output: [[1]]
#
#
#
# Constraints:
#     1 <= nums.length <= 6
#     -10 <= nums[i] <= 10
#     All the integers of nums are unique.


#                                         [1,2,3]
#               1/                          2|                          3\
#           [1],[2,3]                     [2],[13]                     [3],[12]
#           2/    3\                    1/       3\                   1/      2\
#        [12][3]  [13][2]             [21][3]    [23][1]          [31][2]     [32][1]
#         3/         2\               3/            1\              2/          1\
#       [123]        [132]          [213]           [231]         [312]         [321]


# Note: no start index - no ordering, but use an array to keep track which is used
# no duplicated elements


class Solution:
    def permute(self, nums):
        result = []
        self.backtracking(nums, [], [False] * len(nums), result)
        return result

    def backtracking(self, nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = False

