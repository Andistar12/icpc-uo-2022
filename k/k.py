r, k = map(int, input().split(" "))
n = 2 ** r

rr = [int(input()) for _ in range(n)]
print(k)

rr = sorted(rr)

close = 0
def i(aa):
    global close
    half = len(aa) // 2

    for idx in range(half):
        print(aa[idx], aa[len(aa) - idx - 1])
        if abs(aa[idx] - aa[len(aa) - idx - 1]) <= k:
            close += 1

    if len(aa) > 2:
        i(aa[half + 1:])

i(rr)
print(close)
