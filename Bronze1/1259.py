# 펠린드롬수 기러기 스위스 
ans=""
while True:
    num = input()
    if num == "0" :
        break
    for i in range(len(num)//2):
        if num[i] != num[len(num)//2+1+i]:
            ans="no"
            break
    if ans!="no":
        print("yes")
    else:
        print("no")