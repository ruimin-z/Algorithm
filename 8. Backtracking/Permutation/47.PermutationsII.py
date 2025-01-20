# 47. Permutation II - https://leetcode.com/problems/permutations-ii/description/
#
# Given a collection of numbers, nums, that might contain duplicates,
# return all possible unique permutations in any order.
#
# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Constraints:
#     1 <= nums.length <= 8
#     -10 <= nums[i] <= 10


from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(0, len(nums)):
                if used[i]: continue # has been selected in path
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i]=True
                backtrack(path+[nums[i]],used)
                used[i]=False
        backtrack([], [False]*len(nums))
        return res
