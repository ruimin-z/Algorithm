# https://leetcode.com/problems/combination-sum-ii/description/

# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
#
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]

# ----------------------------------------------------------------------
# Logic:
# Remove duplicated path. e.g. candidates=[1,1,7], target=8. Output: [1,7]

# Incorrect ways:
# 1. convert result to set (exceeds time limit!)
# 2. check if path exists in result before append (exceeds time limit!)

# Should be thinking...
# 1. remove duplicates in tree layers 树层去重
# 2. remove duplicates at branch 树枝去重
# In this question, duplicates are allowed at branches. But we remove duplicates in layers

# e.g. candidates=[1,1,2], target=3
#                                                                 visited=[0,0,0], candidates=[1,1,2]
#                               1/                                                     1|                   2\
#                path=[1],visited=[1,0,0],[1,2]                          path=[1],visited=[0,1,0],[2]       path=[2],[0,0,1],[]
#                 1/                     2\                                            2|                       x
# path=[1,1],visited=[1,1,0],[2]        path=[1,2],visited=[1,0,1],[]    path=[1,2],visited=[0,1,1],[]
#   x                                       √                                   √

# 1. sort -> make same elements next to each others
# 2. if current candidate is same as prev, then ignore

# Pseudo Code:
# path - 1d array
# results - 2d array
# def backtrack(candidates, target_sum, current_sum, path, start_index, visited):
#   if (current_sum > target_sum): terminate
#   if (current_sum = target_sum): add path, terminate
#   for (start_index <= i < candidates.length):
#       # remove duplicates: remove if prev index is not visited && current index num == prev index num
#       if( i> start_index and num_at_index_i == num_at_index_i-1 and visited[i-1]==0): continue the for loop
#       update current_sum, visited, path
#       backtrack(..,..,..,i+1,..)
#       reset current_sum, visited, path

# It is ok to not use visited structure.


from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort() # sort
        def backtrack(path, start_index):
            if sum(path) > target:
                return
            if sum(path) == target:
                result.append(path[:])
                return
            for i in range(start_index, len(candidates)):
                # remove duplicates in layers
                if (i > start_index and candidates[i]==candidates[i-1]):
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(path, i+1)
                path.pop()
        backtrack([], 0)
        return result