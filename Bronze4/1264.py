moem = ['a', 'e', 'i', 'o', 'u' ]

while True:
    a = input().lower()
    b=0
    if a == '#':
        break
    for i in moem:
        b += a.count(i)       
    print(b)
