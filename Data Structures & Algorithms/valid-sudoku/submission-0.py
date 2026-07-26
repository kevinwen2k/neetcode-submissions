class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {}
        columns = {}
        for i, row in enumerate(board):
            row_dict = {}
            box_row = i // 3
            if boxes.get(box_row) is None:
                boxes[box_row] = {}
            for j, cell in enumerate(row):
                if cell == '.':
                    continue

                # row check
                if row_dict.get(cell) is not None:
                    return False
                row_dict[cell] = 1

                # column check (inline — no second loop)
                if columns.get(j) is None:
                    columns[j] = set()
                if cell in columns[j]:
                    return False
                columns[j].add(cell)

                # box check
                box_col = j // 3
                if boxes[box_row].get(box_col) is None:
                    boxes[box_row][box_col] = []
                if cell in boxes[box_row][box_col]:
                    return False
                boxes[box_row][box_col].append(cell)

        return True





        