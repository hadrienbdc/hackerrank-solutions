#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    n_bin = format(n, 'b')
    count = 0
    max_num = 0
    for char in n_bin:
        if char == '1':
            count += 1
            if count > max_num:
                max_num = count
        else:
            count = 0

    print(max_num)
