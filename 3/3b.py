# The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the static friction of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

# Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.

# The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

# Consider again the example from before:

# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# Now, the joltages are much larger:

# In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
# In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
# In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
# In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.
# The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.


def main(banks: list[str]):
    joltage_tot = 0
    for bank in banks:
        joltage = maximize_bank(bank)
        print(f'Bank {bank} -> {joltage}')
        joltage_tot += joltage
    print(f'Maxmized {joltage_tot=}')


def maximize_bank(bank: str, bits=12) -> int:
    vals = [0] * bits

    remaining = len(bank) - 1
    for i in range(len(bank)):
        num = int(bank[i])

        # 0, 1, 2, ..., 11
        for bit in range(bits):
            if num > vals[bit]:
                # ensure remaining space
                needed_bits = bits - bit - 1
                if remaining >= needed_bits:
                    vals[bit] = num
                    vals[bit+1:] = [0] * (bits - bit - 1)
                    break
        remaining -= 1

    return int(''.join([str(n) for n in vals]))




if __name__ == '__main__':
    import sys
    inp = sys.argv[-1]
    with open(inp) as f:
        banks = [fline.strip() for fline in f.readlines()]
    main(banks)