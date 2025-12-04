def main():
    ...


if __name__ == '__main__':
    import sys
    with open(sys.argv[-1]) as f:
        data = [fline.strip() for fline in f.readlines()]
    main(data)