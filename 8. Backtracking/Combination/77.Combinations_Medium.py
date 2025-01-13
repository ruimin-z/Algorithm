# https://leetcode.com/problems/combinations/
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

# Constraints:
#     1 <= n <= 20
#     1 <= k <= n


# ----------------------------------------------
# First, decide to use backtrack
# n = 4, k = 4
#                      [1, 2, 3, 4]
#             /        |          |       \
#         take 1     take 2    take 3    take 4
#           /          |          |         \
#        [2,3,4]     [3,4]       [4]         []
#       /    \         |          |           \
#   take2   take3   X(prune)  X(prune)    X(prune)
#     /        \
#   [3,4]      [4]
#     |          \
#   take3        X(prune)
#     |
#    [4]
#     |
#   take4
#     |
#   [], return [1,2,3,4]

# 1. determine params and return:
# 2. determine termination condition
# 3. determine choices in each layer

# Note:
# - Must include start_index in backtracking params: no repetition like [1,1]
# - Using i+1 rather than start_index+1 when calling backtracking: no decreasing list like [4,3]
# - Optimization in for loop range: prune(early stop), last number to consider:  n - (k - len(path)) + 1


from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # save result
        self.backtracking(n, k, 1, [], result)
        return result

    def backtracking(self, n, k, start_index, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start_index, n - (k - len(path)) + 2):  # optimization
            path.append(i)  # process node
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # remove node