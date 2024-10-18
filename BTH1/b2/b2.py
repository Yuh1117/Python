n = 5
a = []
for i in range (n):
    a.append(int(input(f"a[{i}] = ")))
print(a)

d = [x for x in a if x > 0]
print(max(d) if len(d) > 0 else "*")
f = [x for x in a if x < 0]
print(min(f) if len(f) < 0 else "*")

for x in set(a):
    print(f"{x} xuat hien {a.count(x)} lan")

a.sort(reverse=True)
print(a)

