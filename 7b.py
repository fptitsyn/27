f = open("27-7b.txt")
n = f.readline()
a = [int(i) for i in f]
b = [i for i in a if i % 7 == 0 and i % 49 != 0]
c = [i for i in a if i % 7 != 0]

print(max(b) * max(c))
