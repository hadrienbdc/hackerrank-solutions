# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range(T):
    word = input()
    word_even = ''
    word_odd = ''
    for i, char in enumerate(word):
        if i % 2 == 0:
            word_even += char
        else:
            word_odd += char

    print(word_even, word_odd)
