n = int(input())
for _ in range(n):
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        w = word[0] + str(len(word) - 2) + word[len(word)-1]
        print(w)




