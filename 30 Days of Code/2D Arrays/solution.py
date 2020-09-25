#!/bin/python3

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    list_hourglass_sum = []
    for i in range(4):
        for j in range(4):
            hourglass = []
            for (n1) in range(3):
                for (n2) in range(3):
                    if (n1 == 1) and (n2 !=1):
                        continue
                    else:
                        hourglass.append(arr[i+n1][j+n2])
            hourglass_sum = sum(hourglass)
            list_hourglass_sum.append(hourglass_sum)

    result = max(list_hourglass_sum)
    print(result)
