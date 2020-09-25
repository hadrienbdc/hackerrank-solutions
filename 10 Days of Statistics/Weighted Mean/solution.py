# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
ar = list(map(float, input().split()))
weigths = list(map(float, input().split()))

pond_mean = 0

for elem, w in zip(ar, weigths):
    pond_mean += elem * w

pond_mean /= sum(weigths)

print(round(pond_mean, 1))
