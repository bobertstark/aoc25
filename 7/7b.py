def main(grid: list[str]):
    lines = len(grid)
    traveled = {}

    def travel(line, pos) -> int:
        if line >= lines:
            return 0

        if (line, pos) in traveled:
            return traveled[(line, pos)]

        cur = line
        while cur < lines:
            if grid[cur][pos] == '^':
                res = (
                    1 +
                    travel(cur+1, pos-1) +
                    travel(cur+1, pos+1)
                )
                traveled[(line, pos)] = res
                return res
            cur += 1

        traveled[(line, pos)] = 0
        return 0

    timelines = 1 + travel(1, grid[0].index('S'))
    print(timelines)


if __name__ == '__main__':
    import sys
    with open(sys.argv[-1]) as f:
        data = [fline.strip() for fline in f.readlines()]
    main(data)
