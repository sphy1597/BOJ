
num = [int(i) for i in input().split() ]
num.sort()

i = num[2]

while True:
    i+=1
    cnt = 0
    for j in range(5):
        if i % num[j] == 0:
            cnt += 1
    if cnt >= 3:
        break

print(i)