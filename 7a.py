f = open("27-7a.txt")
n = f.readline()
a = [int(i) for i in f]
mr = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        r = a[i] * a[j]
        if r % 7 == 0 and r % 49 != 0:
            mr = max(mr, r)

print(mr)
