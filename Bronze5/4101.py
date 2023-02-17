# while(i:=input())>'1':print('NYoe s'[eval(i.replace(*' >'))::2])

while True:
    num = [int(i) for i in input().split()]
    if num[0]==0 and num[1] == 0:
        break 
    elif num[0] <= num[1]:
        print("No")
    else:
        print("Yes")
