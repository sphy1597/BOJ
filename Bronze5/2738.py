size = [int(i) for i in input().split()]
matrix = list()
for i in range(size[0]*2):
    matrix.append( [int(i) for i in input().split()] )
for i in range(size[0]):
    result = [x+y for x,y in zip(matrix[i], matrix[i+size[0]])]
    string = ""
    for a in range(size[1]):
        string = string + str(result[a]) + " "
    print(string)
