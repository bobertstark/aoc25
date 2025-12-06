def main(ops: list[str]):
    total = 0

    for op in ops:
        total += operate(op[:-1], op[-1])
    print(total)

def mult(nums: list):
    prod = nums[0]
    for num in nums[1:]:
        prod *= num
    return prod

def operate(nums: list[str], operation: str):

    if operation == '+':
        op = sum
    elif operation == '*':
        op = mult
    else:
        raise NotImplementedError
    return op(nums)


def decode(data: list[str]):
    lines = len(data) - 1
    chars_per_line = len(data[0]) - 1

    def get_num(char_pos: int) -> int:
        # ignore last line
        num = ''
        for ln in range(lines):
            char = data[ln][char_pos]
            num += char if char != ' ' else ''
        return int(num)

    operations = []
    nums = []

    i = 0
    while i <= chars_per_line:
        nums.append(get_num(i))
        if (operator := data[len(data)-1][i]) in '+*':
            nums.append(operator)
            operations.append(nums)
            nums = []
            i += 1  # skip next blank col
        i += 1

    main(operations)

if __name__ == '__main__':
    import sys
    with open(sys.argv[-1]) as f:
        data = [ln[::-1].replace('\n', '') for ln in f.readlines()]
        # symbol location matches leftside of largest number

    decode(data)
    #print(data)
    #main(data)