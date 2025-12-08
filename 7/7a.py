def main(grid: list[str]):

    splits = 0

    for row in range(1, len(grid)):
        for col in range(len(grid[0])):

            if grid[row-1][col] not in 'S|':
                continue

            if grid[row][col] == '^':
                was_split = False
                for i in (-1, 1):
                    val = grid[row][col+i]
                    if val == '.':
                        grid[row][col+i] = '|'
                        was_split = True
                splits += int(was_split)
            else:
                grid[row][col] = '|'

    print(splits)



if __name__ == '__main__':
    import sys
    with open(sys.argv[-1]) as f:
        data = [list(fline.strip()) for fline in f.readlines()]
    main(data)
