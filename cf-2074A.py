t = int(input())
for _ in range(t):
    l, r, d, u = input().split()
    l = abs(int(l))
    r = abs(int(r))
    d = abs(int(d))
    u = abs(int(u))
    if (l == r and d == u and l == u):
        print('YES')
    else:
        print('NO')
