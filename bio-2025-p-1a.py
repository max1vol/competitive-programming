def run():
    pn = int(input())
    palis = []
    ns = str(pn)
    if list(ns) == list(reversed(ns)):
        print(pn)
        return
    for n in range(1, pn):
        ns = str(n)
        if list(ns) == list(reversed(ns)):
            palis.append(n)
    for n in palis:
        if pn - n in palis:
            print(n, pn - n)
            return
    for n1 in palis:
        for n2 in reversed(palis):
            if pn - n1 - n2 in palis:
                print(n1, n2, pn - n1 - n2)
                return


run()




