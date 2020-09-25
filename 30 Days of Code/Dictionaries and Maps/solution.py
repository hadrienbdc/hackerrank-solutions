# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phone_book = {}

for i in range(n):
    input_ = input().split()
    name = input_[0]
    phone = input_[1]
    phone_book[name] = phone

while True:
    try:
        name2 = input()
        if name2 in phone_book.keys():
            print(name2 + '=' + phone_book[name2])
        else:
            print('Not found')
    except Exception:
        break
