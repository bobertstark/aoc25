def main(rotations: list):
    zeroed = 0
    cur_pos = 50

    while rotations:
        rot = rotations.pop(0)
        lr_dir, dist = rot[0], int(rot[1:])
        new_pos, zeroes = move(cur_pos, lr_dir, dist)
        print(f'Moved {rot} ({cur_pos}->{new_pos}), zeroes during move: {zeroes}')
        cur_pos = new_pos
        zeroed += zeroes

    print(f'Number of 0 positions: {zeroed}')
    return zeroed


def move(cur_pos: int, lr_dir: str, dist: int) -> tuple[int, int]:
    zstart = cur_pos == 0
    # If distance is larger than 100, count laps
    zeroes = 0
    if dist >= 100:
        zeroes += (dist // 100)
        dist %= 100

    if lr_dir == "L":
        dist *= -1

    cur_pos += dist
    if (not zstart and cur_pos <= 0) or cur_pos > 99:
        zeroes += 1

    cur_pos %= 100
    return cur_pos, zeroes


if __name__ == "__main__":
    import sys

    rots = sys.argv[-1]
    with open(rots) as f:
        rotations = [line.strip() for line in f.readlines()]
    main(rotations)
