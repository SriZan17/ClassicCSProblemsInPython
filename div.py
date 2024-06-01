def main():
    n = 1
    while True:
        if n % 6 == 0 and n % 7 == 0 and n % 8 == 0 and n % 9 == 0 and n % 10 == 0:
            print(n)
            break
        n += 1


if __name__ == "__main__":
    main()
