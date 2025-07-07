n = int(input())
c = input().split()
s = 0
d = 0
for i in range(n):
    c[i] = int(c[i])
for i in range(n // 2):
    if c[len(c) - 1] > c[0]:
        s = s + c.pop()
    else:
        s = s + c.pop(0)
    if c[len(c) - 1] > c[0]:
        d = d + c.pop()
    else:
        d = d + c.pop(0)
for _ in range(n % 2):
    s = s + c.pop()
print(s, d)



