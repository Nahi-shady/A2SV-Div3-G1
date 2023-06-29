def countSwaps(a):
    # Write your code here
    count = 0
    for i in range(len(a) - 1):
        swapped = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
                swapped = True
        if not swapped:
            break
    print(f'Array is sorted in {count} swaps. \nFirst Element: {a[0]} \nLast Element: {a[-1]}')


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)