f = open("27-13a.txt")

n = f.readline()

a = [int(i) for i in f]
c = 0

for i in range(len(a) - 7):
    for j in range(i + 7, len(a)):
        if (a[i] * a[j]) % 14 == 0:
            c += 1

print(c)
