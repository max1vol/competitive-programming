from tqdm import tqdm

def run():
    palis = []
    N = 1_000_000
    for n in range(1, N):
        ns = str(n)
        if list(ns) == list(reversed(ns)):
            palis.append(n)
    palis = set(palis)
    print(f"Found {len(palis)} palindromes under {N}")

    def is_pali(n):
        if n in palis:
            return True
        return False

    def is_pali2(n):
        for n2 in palis:
            if n - n2 in palis:
                return True
        return False

    c = 0
    for n in tqdm(range(1, N+1)):
        if not is_pali(n) and not is_pali2(n):
            c = c + 1
    print(c)


run()




