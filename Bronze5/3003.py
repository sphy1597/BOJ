chess = [1, 1, 2, 2, 2, 8]
mychess = [int(i) for i in input().split()]
string = ""
for a in range(6):
    string += str(chess[a]-mychess[a]) + " "
print(string)
