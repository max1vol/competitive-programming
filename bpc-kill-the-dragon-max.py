# H, T = input().split()
# T = int(T)
# H = int(H)


def min_path(h, t):
    l = [[h, t, []]]
    while True:
        for state in l:
            if state[0] == 0 and state[1] == 0:
                return state[2]
        nl = []
        for s in l:
            h, t, p = s
            if t >= 1:
                nl.append([h, t + 1, p + ['T']])
                if t >= 2:
                    nl.append([h + 1, t - 2, p + ['TT']])
            if h >= 1:
                nl.append([h - 1, t + 1, p + ['H']])
                if h >= 2:
                    nl.append([h - 2, t, p + ['HH']])
        l = nl

ra = min_path(3, 1)
for t in ra:
    print(t)










