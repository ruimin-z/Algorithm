# https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
#
# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
#
# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#
# Example 3:
# Input: candidates = [2], target = 1
# Output: []

# ------------------------------------
# e.g. candidates=[2,5,3], target=4
#                                     [2,5,3]
#                    2/                 5|            3\
#                [2],[2,5,3]         [5],[5,3]        [3],[]
#        2/         5|         3\
# [2,2],[2,5,3]    [2,5],[5,3]   [2,3],[]
#   √               x              x

# Note:
# 0. question said no duplicate candidates. Otherwise, need to think about removing duplicates
# 1. allow repetition in the list - permutation
# 2. use start index to track candidates from left to right, but since we allow repetition, use i rather than i+1 when backtracking
# 3. Tree depth is fixed by the target sum and candidate components

# Logic:
# 1. return and params - 2d array result, 1d array path
# 2. termination condition
# 3. logic in each search layer

# Optimization - pruning
# 1. sort candidates
# 2. prune - if current candidate > target, prune this and the rest candidates


from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(candidates, target, path, start_index):
            if sum(path) > target:
                return
            if sum(path) == target:
                result.append(path[:])
                return
            for i in range(start_index, len(candidates)):
                path.append(candidates[i])
                backtrack(candidates, target, path, i) # i bc allow repetition
                path.pop()
        backtrack(candidates, target, [], 0)
        return result

    def combinationSumOptimized(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort() # sort
        def backtrack(candidates, target, path, start_index):
            if sum(path) > target:
                return
            if sum(path) == target:
                result.append(path[:])
                return
            for i in range(start_index, len(candidates)):
                if sum(path) + candidates[i] > target: # prune
                    break
                path.append(candidates[i])
                backtrack(candidates, target, path, i)
                path.pop()
        backtrack(candidates, target, [], 0)
        return result


