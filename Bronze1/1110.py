# 더하기 사이클 
num = int(input())
quotient, remainder = divmod(num,10)
cnt = 0
while(True):
    cnt+=1
    answer = quotient + remainder
    quotient = remainder
    remainder = answer%10
    if(quotient*10+remainder == num):
        break
      
print(cnt)