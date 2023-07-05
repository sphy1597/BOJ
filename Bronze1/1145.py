# 적어도 대부분의 배수

num = [int(i) for i in input().split(" ")]
num.sort()

cnt = 0
i = num[2]
while True:
    
    for j in range(5):
        if i % num[j] == 0:
            cnt += 1
    if cnt >= 3:
        break
    
    cnt = 0   
    i += 1
    
print(i)