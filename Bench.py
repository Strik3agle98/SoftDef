import time

if __name__ == "__main__":
    f = open("result.txt", "w")
    l = list()
    start = time.time_ns()
    for i in range(50001):
        l.append([i, (time.time_ns() - start)/(10**9)])

    for e in l:
        f.write(str(e[0]) + " " + str(e[1]) + "\n")

    toprint = list()
    for a in range(50001):
        if a % 5000 == 0:
            toprint.append(l[a][1])
    print(toprint)
