def main(ranges: list[range], items: list[int]):
    fresh = 0

    def is_fresh(item: int) -> bool:
        for rang in ranges:
            if item in rang:
                return True
        return False

    for item in items:
        if is_fresh(item):
            fresh += 1
    print(fresh)

if __name__ == '__main__':
    import sys

    ranges = []
    with open(sys.argv[-1]) as f:
        rangs, items = f.read().split('\n\n')
        for r in rangs.strip().split('\n'):
            start, end = r.split('-')
            ranges.append(range(int(start), int(end) + 1))
        items = [int(x) for x in items.strip().split('\n')]
    main(ranges, items)