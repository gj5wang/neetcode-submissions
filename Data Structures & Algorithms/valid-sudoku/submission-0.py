class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                #create thes et if its not created yet
                if r not in rows:
                    rows[r] = set()

                if c not in cols:
                    cols[c] = set()
            
                num = board[r][c]

                if num == ".":
                    continue

                if num in rows[r]:
                    return False
                else:
                    rows[r].add(num)
                
                if num in cols[c]:
                    return False
                else:
                    cols[c].add(num)
                
                box = (r//3, c//3)
                if box not in boxes:
                    boxes[box]= set()
                
                if num in boxes[box]:
                    return False
                else:
                    boxes[box].add(num)
        return True

                



