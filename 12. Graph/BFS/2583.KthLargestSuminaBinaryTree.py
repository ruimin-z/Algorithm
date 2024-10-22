# You are given the root of a binary tree and a positive integer k.
# The level sum in the tree is the sum of the values of the nodes that are on the same level.
# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
# Note that two nodes are on the same level if they have the same distance from the root.


# BFS - QUEUE - FIFO
# Time: traverse each node O(V) + sum O(V) + sort O(LlogL) =  O(V+LlogL)
# Space: total_sum O(2V) + level_sums O(V) + fringe O(logV) = O(V)
# fringe 等比数列 Geometric Series,
# V = sum of nodes at each level
#   = 1 + 2 + 4 + 8 + 16 +...
#   = a(1-r^n)/(1-r) where a=1 is first term, r=2 is ratio, n is # of terms
# V = 2^n - 1
# n = log_2(V-1)


# Faster: MaxHeap or MinHeap

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthLargestLevelSum(root: Optional[TreeNode], k: int) -> int:
    if not root: return -1

    total_sum = [(0, root.val)]
    fringe = [(root, 0, root.val)]

    while fringe:
        node, level, total = fringe.pop(0)
        for child in (node.left, node.right):
            if child:
                fringe.append((child, level + 1, child.val))
                total_sum.append((level + 1, child.val))

    level_sums = []
    for level, val in total_sum:
        if len(level_sums) <= level:
            level_sums.append(val)
        else:
            level_sums[level] += val
    level_sums.sort(reverse=True)
    return level_sums[k-1] if len(level_sums) >= k else -1

