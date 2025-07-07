m = 12
c = []
while m > 0:
    if m%2 == 0:
        c.append('3')
    else:
        c.append('6')
    m = m//2

print(''.join(reversed(c)))












