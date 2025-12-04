# The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

# So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.

# Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.

# So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.

# The dial starts by pointing at 50.

# You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

# For example, suppose the attached document contained the following rotations:
# L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82


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
