#가장 많이 나온 알파벳

ipt = input().upper()
char = []
cnt = []


while len(ipt) > 0:
    char.append(ipt[0])
    cnt.append(ipt.count(ipt[0]))
    ipt = ipt.replace(ipt[0], "")

if cnt.count(max(cnt))>1:
    print("?")
else:
    print(char[cnt.index(max(cnt))])
    


# print(char)


