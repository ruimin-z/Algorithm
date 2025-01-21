# 51. N-Queens - https://leetcode.com/problems/n-queens/description/
# See another solution at https://programmercarl.com/0051.N%E7%9A%87%E5%90%8E.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E8%A1%A5%E5%85%85

# Rules:
# No two queens in the same row, same column, or on diagonal lines.

# res - 3d array
# 通过递归 控制嵌套for循环的层数
# n*n -> n个for循环

# 3*3 Board
#                           1/                2|           3\
# row1：                 [Q..]               [.Q.]          [..Q]
#                     1/  2|    3\          1/ 2| 3\        1/  2|    3\
# row2:              x    x     [..Q]       x  x   x      [Q..]  x     x
#                               1/2|3\                   1/ 2| 3\
# row3：                         x x x                   x   x   x
# No valid results


# Note:
# - Can also initialize res to 3d array with dots first

# Difficulty:
# 1. no need to check if there is Q in same row
# 2. figure out 135 degree cells indices
# 3. termination condition row=n and len(arrangement)=n both work <- 本以为这里出问题其实没事
# 4. return format

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtrack(n, row, arrangement):
            if row == n: # last row, leaf node
                # print("Found", arrangement)
                res.append(arrangement.copy())
                return
            for col in range(n):
                if self.valid(row, col, arrangement):
                    arrangement.append('.'*col+'Q'+'.'*(n-col-1)) # see Note
                    # print(row, col, "arrangement", arrangement)
                    backtrack(n, row+1, arrangement)
                    arrangement.pop()
        backtrack(n, 0, [])
        return res


    def valid(self, row_id, col_id, arrangement):
        if not arrangement:
            return True
        # Check if Q in same column
        for row_i in range(len(arrangement)):
            if arrangement[row_i][col_id] == 'Q':
                # print(row_id, col_id, "col:",row_i,col_id)
                return False
        # Check if Q in 45 degree or 135 degree
        for i in range(row_id):
            if row_id-i-1 >= 0 and col_id-i-1 >= 0 and arrangement[row_id-i-1][col_id-i-1] == 'Q':
                # print(row_id, col_id, "45:", row_id-i-1, col_id-i-1)
                return False
            if row_id-i-1 >= 0 and len(arrangement[0])> col_id+i+1 >= 0 and arrangement[row_id-i-1][col_id+i+1]== 'Q':
                # print(row_id, col_id, "135:", row_id-i-1, col_id+i+1)
                return False
        return True

