#어떤수 n의 약수의 게수와 약수들이 주어 졌을 때 n을 구해라

cnt = int(input())
divisor = [int(i) for i in input().split()]
divisor.sort()
print(divisor[0]*divisor[cnt-1])