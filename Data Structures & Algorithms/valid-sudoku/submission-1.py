class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checklist_x = [True for _ in range(9)]

        for y in range(9):
            number_list = [0 for _ in range(9)]

            for x in range(9):
                if board[y][x] != ".":
                    index = int(board[y][x]) - 1
                    number_list[index] += 1

            if any(z >= 2 for z in number_list):
                checklist_x[y] = False

        checklist_y = [True for _ in range(9)]

        for x in range(9):
            number_list = [0 for _ in range(9)]

            for y in range(9):
                if board[y][x] != ".":
                    index = int(board[y][x]) - 1
                    number_list[index] += 1

            if any(z >= 2 for z in number_list):
                checklist_y[x] = False

        checklist_block = [[True for _ in range(3)] for _ in range(3)]

        for block_y_index in range(3):
            for block_x_index in range(3):
                number_list = [0 for _ in range(9)]

                for y in range(block_y_index * 3, block_y_index * 3 + 3):
                    for x in range(block_x_index * 3, block_x_index * 3 + 3):
                        if board[y][x] != ".":
                            index = int(board[y][x]) - 1
                            number_list[index] += 1

                if any(z >= 2 for z in number_list):
                    checklist_block[block_y_index][block_x_index] = False

        if (
            all(checklist_x)
            and all(checklist_y)
            and all(all(cell for cell in row) for row in checklist_block)
        ):
            return True
        else:
            return False