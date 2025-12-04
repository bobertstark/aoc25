def main(banks: list[str]):
    joltage_tot = 0
    for bank in banks:
        joltage = maximize_bank(bank)
        print(f'Bank {bank} -> {joltage}')
        joltage_tot += joltage
    print(f'Maxmized {joltage_tot=}')


def maximize_bank(bank: str) -> int:
    "Max: 99, Min: 11"
    tens, ones = 0, 0

    for i in range(len(bank)):
        used = False
        num = int(bank[i])
        if num > tens:
            if i != (len(bank) - 1):
                tens = num
                ones = 0
                used = True

        if not used and num > ones:
            ones = num
    return tens * 10 + ones




if __name__ == '__main__':
    import sys
    inp = sys.argv[-1]
    with open(inp) as f:
        banks = [fline.strip() for fline in f.readlines()]
    main(banks)