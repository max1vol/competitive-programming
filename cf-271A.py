yi = int(input())
while True:
    yi = yi + 1
    y = str(yi)
    if y[0] != y[1] and y[2] != y[1] and y[2] != y[0] and y[3] != y[2] and y[3] != y[1] and y[3] != y[0]:
        print(yi)
        break
