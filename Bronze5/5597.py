a = list(range(1,31))
for i in range(28):
    a.remove(int(input()))
print(a[0])
print(a[1])

#숏코딩
print(*{*map(int,open(0))}^{*range(1,31)})
