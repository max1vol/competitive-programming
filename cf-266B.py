n,t = input().split()
n = int(n)
t = int(t)
q = input()
cq = []
for e in q:
    cq.append(e)
for _ in range(t):
    i = 0
    while i + 1 < n:
        if cq[i] == 'B' and cq[i + 1] == 'G':
            cq[i] = 'G'
            cq[i + 1] = 'B'
            i = i + 2
        else:
            i = i + 1
for i in range(n):
    print(cq[i],end='')


