def min_node_diff(n):
    mn = abs(n[0] - n[len(n) - 1])
    for i in range(0, len(n)):
        pi = i + 1
        if i == pi:
            continue
        mn = min(mn, abs(n[i] - n[pi]))
    return mn


ra = []


def array(r):
    if r is None:
        return
    ra.append(r.val)
    array(r.left)
    array(r.right)


# array(root)
# return (min_node_diff(ra))






