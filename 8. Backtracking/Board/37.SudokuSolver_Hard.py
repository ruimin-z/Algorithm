# 37. Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

# 1. Return Type
# Different from backtracking:
# Once found one result, immediately stop searching.
# But in other backtracking we have done, we find all possible results.

# From Path Sum in Binary Search:
# Search whole tree structure -> return type void (Multiple Paths)
# Search single branch -> return type bool ✅ (Single Path)


# 2. Termination Condition:
# No need to write it out. Once the grid is full, the search stops.


# Logic:
# - 2 layers for loops: row and col

from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(board) -> bool:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        for k in range(1,10):
                            if self.isValid(i, j, str(k), board):
                                board[i][j] = str(k)
                                res = backtrack(board)
                                if res:
                                    return True # 找到结果立刻return，不再继续搜索
                                board[i][j] = '.' # 回溯
                        else:
                            return False
            return True # If never hit return false, then all nums are placed correctly and filled the grid
        backtrack(board)


    def isValid(self, row, col, val, board):
        # check row
        for i in range(len(board[0])):
            if board[i][col] == val: return False
        # check col
        if val in board[row]:
            return False
        # check box
        start_row, start_col = (row//3)*3, (col//3)*3
        for i in range(start_row, start_row+3):
            for j in range(start_col, start_col+3):
                if board[i][j] == val:
                    return False
        return True


problem = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
solver = Solution()
solver.solveSudoku(problem)
print(problem)

# The above method works well in java but exceed time limit only in Python
# The following does not exceed the time limit
# Added: - use set to optimize row, col, block
#        - index for retrieving blocks

class SolutionOptimized:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_used = [set() for _ in range(9)]
        col_used = [set() for _ in range(9)]
        box_used = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                row_used[row].add(num)
                col_used[col].add(num)
                box_used[(row // 3) * 3 + col // 3].add(num)
        self.backtracking(0, 0, board, row_used, col_used, box_used)

    def backtracking(
        self,
        row: int,
        col: int,
        board: List[List[str]],
        row_used: List[Set[str]],
        col_used: List[Set[str]],
        box_used: List[Set[str]],) -> bool:
        if row == 9:
            return True
        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)

        if board[row][col] != ".":
            return self.backtracking(
                next_row, next_col, board, row_used, col_used, box_used
            )

        for num in map(str, range(1, 10)):
            if (
                num not in row_used[row]
                and num not in col_used[col]
                and num not in box_used[(row // 3) * 3 + col // 3]
            ):
                board[row][col] = num
                row_used[row].add(num)
                col_used[col].add(num)
                box_used[(row // 3) * 3 + col // 3].add(num)
                if self.backtracking(
                    next_row, next_col, board, row_used, col_used, box_used
                ):
                    return True
                board[row][col] = "."
                row_used[row].remove(num)
                col_used[col].remove(num)
                box_used[(row // 3) * 3 + col // 3].remove(num)
        return False
