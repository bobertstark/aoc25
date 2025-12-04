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