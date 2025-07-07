n,m,a = input().split()
n = int(n)
m = int(m)
a = int(a)
n1 = n//a
if n%a > 0:
    n1 = n1 + 1
m1 = m//a
if m%a > 0:
    m1 = m1 + 1
print(m1 * n1)


