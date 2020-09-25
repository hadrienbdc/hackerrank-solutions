# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
ar = sorted(list(map(int, input().split())))

mid = int(n / 2)
if n % 2 == 0:
    q2 = (ar[mid] + ar[mid-1]) / 2
    l_half = ar[:mid]
    u_half = ar[mid:]
else:
    q2 = ar[mid]
    l_half = ar[:mid]
    u_half = ar[mid+1:]

mid = int(len(l_half) / 2)
if len(l_half) % 2 == 0:
    q1 = (l_half[mid] + l_half[mid-1]) / 2
else:
    q1 = l_half[mid]

mid = int(len(u_half) / 2)
if len(u_half) % 2 == 0:
    q3 = (u_half[mid] + u_half[mid-1]) / 2
else:
    q3 = u_half[mid]

print(int(q1))
print(int(q2))
print(int(q3))
