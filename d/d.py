import math

n = int(input())

probs = []
for _ in range(n):
    probs.append(float(input()))

thres = []
for _ in range(n):
    thres.append(int(input()))

plus = 1
minus = 1

ITERS = 20

ps = sorted(probs)

prob_highest = 1
prob_lowest = 1

for count, p in enumerate(ps):
    temp = 1
    f = 0
    for _ in range(ITERS):
        temp = temp * p * (1-p)
        f += temp

    prev = thres[count - 1] if count > 0 else 0

    iters_hh = thres[count] - prev
    prob_hh = prob_highest * math.pow(p, iters_hh) * f
    prob_ll = prob_lowest * math.pow(p, iters_hh) * f

    iters_lh = thres[count] + prev
    prob_lh = prob_lowest * math.pow(1-p, iters_lh) * f
    prob_hl = prob_highest * math.pow(1-p, iters_lh) * f

    prob_highest = prob_hh + prob_lh
    prob_lowest = prob_hl + prob_ll

    print(prob_highest)
    print(prob_lowest)

print()
print(prob_highest)

