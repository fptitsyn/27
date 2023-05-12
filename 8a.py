f = open("27-8a.txt")

n = f.readline()
a = [int(i) for i in f]

ms = 10000000000000000000000000000000
for i in range(len(a) - 5):
    for j in range(i + 5, len(a)):
        ms = min(ms, a[i] ** 2 + a[j] ** 2)

print(ms)
