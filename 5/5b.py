# LOL no - ranges are massive
# def main(ranges: list[range]):
#     fresh = set()

#     for rang in ranges:
#         for n in rang:
#             fresh.add(n)
#     print(len(fresh))

# {min: max}

def main(ranges: list[tuple[int, int]]):

    final_ranges = []
    ranges = sorted(ranges) # iterates twice but simplifies logic greatly
    start, stop = ranges.pop(0)

    while ranges:
        istart, istop = ranges.pop(0)
        if istart <= stop + 1:
            stop = max(istop, stop)
        else:
            # start new range
            final_ranges.append((start, stop))
            start, stop = istart, istop
    else:
        # once exhausted, add final range
        final_ranges.append((start, stop))

    count = 0
    for minn, maxx in final_ranges:
        rng = range(minn, maxx+1)
        count += len(rng)
    print(count)


if __name__ == '__main__':
    import sys

    ranges = []
    with open(sys.argv[-1]) as f:
        rangs, _ = f.read().split('\n\n')

        for r in rangs.strip().split('\n'):
            start, end = r.split('-')
            ranges.append((int(start), int(end)))
    main(ranges)