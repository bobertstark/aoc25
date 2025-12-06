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

    nums = [int(n) for n in nums]
    return op(nums)

if __name__ == '__main__':
    import sys
    with open(sys.argv[-1]) as f:
        data = []
        for fline in f.readlines():
            data.append([x for x in fline.strip().split(' ') if x != ''])

        data = list(zip(*data))
    print(data)
    main(data)