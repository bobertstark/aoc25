def is_invalid(num: str) -> bool:
    midpoint = len(num) // 2
    return num[:midpoint] == num[midpoint:]

def main(ranges: list[tuple[str, str]]) -> int:
    invalid_tot = 0

    for start, end in ranges:
        for num in range(int(start), int(end) + 1):
            if is_invalid(str(num)):
                print('Found invalid ID:', num)
                invalid_tot += num
    print('Total invalid IDs sum to:', invalid_tot)
    return invalid_tot



if __name__ == "__main__":
    import sys
    inp = sys.argv[-1]
    with open(inp) as f:
        ranges = [x.split('-') for x in f.read().strip().split(",")]
    print(ranges)
    main(ranges)
