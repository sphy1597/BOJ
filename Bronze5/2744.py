#print(input().swapcase())

s = list(input())
for i in range(len(s)):
    if s[i].isupper():
        s[i] = s[i].lower()
    else:
        s[i] = s[i].upper()
print(''.join(s))
