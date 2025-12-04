def is_invalid(num: str) -> bool:
    for segs in range(1, len(num)):
        if len(num) % segs != 0:
            continue
        if check_segments(num, segs):
            return True
    return False


def check_segments(num: str, segs: int) -> bool:
    seg_idx = segs

    cur_seg = num[:seg_idx]
    while seg_idx < len(num):
        next_idx = seg_idx + segs
        next_seg = num[seg_idx:next_idx]
        if cur_seg != next_seg:
            return False
        seg_idx = next_idx
    return True


def main(ranges: list[tuple[str, str]]) -> int:
    invalid_tot = 0

    for start, end in ranges:
        for num in range(int(start), int(end) + 1):
            if is_invalid(str(num)):
                print('Found invalid ID:', num)
                invalid_tot += num
    print('\nTotal invalid IDs sum to:', invalid_tot)
    return invalid_tot



if __name__ == "__main__":
    import sys
    inp = sys.argv[-1]
    with open(inp) as f:
        ranges = [x.split('-') for x in f.read().strip().split(",")]
    print(ranges)
    main(ranges)
