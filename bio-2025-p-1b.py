def run():
    palis = []
    for n in range(1, 54):
        ns = str(n)
        if list(ns) == list(reversed(ns)):
            palis.append(n)
    for n in palis:
        if 54 - n in palis:
            print(n, 54 - n)
            return
    for n1 in palis:
        for n2 in reversed(palis):
            if 54 - n1 - n2 in palis:
                print(n1, n2, 54 - n1 - n2)


run()




