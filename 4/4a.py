def main(grid):
    MAX_ROW = len(grid) - 1
    MAX_COL = len(grid[0]) - 1

    access_cnt = 0

    def few_neighbors(grid, row, col) -> bool:
        # . . .
        # . @ .
        # . . .
        count = 0

        pots = [
            (row+1, col), (row+1, col+1), (row+1, col-1),
            (row, col+1), (row, col-1),
            (row-1, col), (row-1, col+1), (row-1, col-1),
        ]
        for pr, pc in pots:
            if pr < 0 or pr > MAX_ROW or pc < 0 or pc > MAX_COL:
                continue
            val = grid[pr][pc]
            if val in '@x':
                count += 1
            if count >= 4:
                return False
        return True

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != '@':
                continue
            if few_neighbors(grid, row, col):
                # assign as accessible
                grid[row][col] = 'x'
                access_cnt += 1

    for row in grid:
        print(''.join(row))

    print(f'Accessible: {access_cnt}')


if __name__ == '__main__':
    import sys
    with open(sys.argv[-1]) as f:
        data = [list(fline.strip()) for fline in f.readlines()]
    main(data)