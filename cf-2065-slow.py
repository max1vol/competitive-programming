t = int(input())
for _ in range(t):
    line = input()
    c = False
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            c = True
    if c:
        print(1)
    else:
        print(len(line))

