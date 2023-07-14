# 나머지

num = [int(i) for i in input().split()]
a=num[0]
b=num[1]
c=num[2]
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)