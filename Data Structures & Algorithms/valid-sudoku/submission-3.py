class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #umm logic here
        #check elements in each row, count amount, if >1 then return False
        #do same for each column and each 9*9 subsquare
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] in seen:
                    if board[row][i] == ".":
                        continue
                    else:
                        return False
                seen.add(board[row][i])
        for column in range(9):
            seen = set()
            for row in range(9):
                if board[row][column] in seen:
                    if board[row][column] == ".":
                        continue
                    else:
                        return False
                else:
                    seen.add(board[row][column])
        #3*3 subsuqare
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True