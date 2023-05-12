f = open("27-8b.txt")

n = f.readline()
a = [int(i) for i in f]

k = 5
ms = 10 ** 20
mn = ms
buff = [a[i] for i in range(k)]

for i in range(k, len(a) - k):
    r = buff.pop(0)
    mn = min(mn, r)
    ms = min(ms, mn ** 2 + a[i] ** 2)
    buff.append(a[i])

print(ms)
