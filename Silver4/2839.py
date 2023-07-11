# 설탕 배달
sugar = int(input())

bonji = 0
while sugar >= 0:   
    if sugar % 5 == 0:
        bonji += sugar // 5
        print(bonji)
        break
    sugar -= 3
    bonji += 1

if sugar < 0 :
    print(-1)