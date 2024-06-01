def main():
    print(fibonacci(200))


def fibonacci(n: int) -> int:
    if n == 0:
        return n

    last: int = 0
    nex: int = 1
    for _ in range(1, n):
        # last, nex = nex, last + nex
        # temp = nex
        # nex = last + nex
        # last = temp
        nex, last = last + nex, nex
    return nex


if __name__ == "__main__":
    main()
