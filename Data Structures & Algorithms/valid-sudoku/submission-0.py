class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #analyse each 3x3
        #analyse each column
        #analyse each row
        valid = True
        seen = set() #(a, 'b') or ('a', b)
        seen_box = set() # (a,b,'c')
#row//3 = 1,2,3
#column//3 = 1,2,3

        for row in range(9):
            for column in range(9):
                if board[row][column]!=".":

                    if (row, board[row][column]) not in seen and (board[row][column], column) not in seen and (row//3, column//3, board[row][column]) not in seen_box:
                        seen.add((row, board[row][column]))
                        seen.add((board[row][column], column))
                        seen_box.add((row//3, column//3, board[row][column]))
                    
                    else:
                        return False
                           
        return True

                