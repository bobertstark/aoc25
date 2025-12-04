def main(rotations: list):
    zeroed = 0
    cur_pos = 50

    while rotations:
        rot = rotations.pop(0)
        lr_dir, dist = rot[0], int(rot[1:])
        cur_pos = move(cur_pos, lr_dir, dist)
        if cur_pos == 0:
            zeroed += 1
    print(f'Number of 0 positions: {zeroed}')
    return zeroed


def move(cur_pos: int, lr_dir: str, dist: int) -> int:
    if lr_dir == "L":
        dist = -dist
    cur_pos = (cur_pos + dist) % 100
    return cur_pos


if __name__ == "__main__":
    import sys

    rots = sys.argv[-1]
    with open(rots) as f:
        rotations = [line.strip() for line in f.readlines()]
    main(rotations)
