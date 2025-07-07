t = int(input())
for i in range(t):
    n = int(input())
    if n == 1 or n == 3:
        print(-1)
    else:
        m = 0
        while True:
            m = m + 1
            c = 66*m
            cs = str(c)
            if len(cs) == n:
                isValid = True
                for e in cs:
                    if e != '3' and e != '6':
                        isValid = False
                        break
                if isValid:
                    print(c)
                    break




