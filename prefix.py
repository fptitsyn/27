f = open("27.txt")
n, k = map(int, f.readline().split())
a = [int(i) for i in f]

count = [0] * k
c = 0
s = 0
for i in range(n):
    s += a[i]
    if s % k == 0:
        c += 1
    c += count[s % k]
    count[s % k] += 1
print(c)
