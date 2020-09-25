#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr_reverse = [str(x) for x in arr[::-1]]

    print(' '.join(arr_reverse))
