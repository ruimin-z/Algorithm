# Solution: https://leetcode.com/problems/cousins-in-binary-tree-ii/solutions/5955380/python-simple-bfs-98-t-82-s/

# Complexity
# Time Complexity: O(n)
# Space Complexity: O(n)

# Define siblingsSum = sum of a node's value and its sibling values
# Construct a fringe of queue of tuples: [(node, node's siblingsSum), ...] where the fringe stores nodes at the same level
# Each node has node.val, so we can get the levelSum = sum of all node values
# Then levelSum - siblingsSum => cousinsSum => set to node.val

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        pq = deque()
        pq.append((root, root.val))

        while pq:
            node_count = len(pq)

            # Calculate the sum at this level
            levelSum = sum([node.val for node, _ in pq]) # Tricky!!

            # Traverse each node
            for _ in range(node_count):
                node, siblingsSum = pq.popleft()

                # get the sum of each node's children (sum of siblings)
                childSum = 0
                if node.left: childSum += node.left.val
                if node.right: childSum += node.right.val

                # queue the child nodes with the sum of their siblings
                if node.left: pq.append((node.left, childSum))
                if node.right: pq.append((node.right, childSum))

                # set the current node val to the subtraction of levelSum - siblingSum
                node.val = levelSum - siblingsSum

        return root
