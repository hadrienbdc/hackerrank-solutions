# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
ar = list(map(int, input().split()))
ar = sorted(ar)

mean = 0
med = 0
mode = 0
occ = {}

for elem in ar:
    mean += elem
    if elem in occ:
        occ[elem] += 1
    else:
        occ[elem] = 1

print(mean/n)

if n % 2 == 0:
    m1 = ar[int(n/2 - 1)]
    m2 = ar[int(n/2)]
    med = (m1 + m2) / 2
else:
    med = ar[int(n/2)] / 2

print(med)

mode = max(occ, key=lambda x: occ[x])

print(mode)
