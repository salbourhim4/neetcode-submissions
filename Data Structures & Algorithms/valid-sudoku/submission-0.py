class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        bool_list = []
        def are_rows_valid(board: list[list[str]]) -> bool:
            for lst in board:
                filtered_list = [x for x in lst if x != '.']
        
                if len(filtered_list) != len(set(filtered_list)):
                    return False
    
            return True

        def transpose_board(board: list[list[str]]) -> list[list[str]]:
            transposed = [list(row) for row in zip(*board)]
            return transposed
    
        def linearize_3x3(board: list[list[str]]) -> list[list[str]]:
            lst1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            lst2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            rlist = []
            blist = []
            for w in range(0, 3):
                for k in range(0, 3):
                    for i in range(0, 3):
                        for j in range(0, 3):
                            x = lst1[w][i]
                            y = lst2[k][j]
                            num = board[x][y]
                            rlist.append(num)
                    blist.append(list(rlist))
                    rlist = []
            return blist
        new_board = transpose_board(board)
        linear_boards = linearize_3x3(board)

        bool_list.append(are_rows_valid(board))
        bool_list.append(are_rows_valid(new_board))
        bool_list.append(are_rows_valid(linear_boards))


        if False not in bool_list:
            return True
        return False