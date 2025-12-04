# You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

# As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

# "Due to newer security protocols, please use password method 0x434C49434B until further notice."

# You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

# Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

# The dial starts by pointing at 50.
# The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
# The dial is rotated L30 to point at 52.
# The dial is rotated R48 to point at 0.
# The dial is rotated L5 to point at 95.
# The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
# The dial is rotated L55 to point at 0.
# The dial is rotated L1 to point at 99.
# The dial is rotated L99 to point at 0.
# The dial is rotated R14 to point at 14.
# The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
# In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

# Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

# Using password method 0x434C49434B, what is the password to open the door?


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
