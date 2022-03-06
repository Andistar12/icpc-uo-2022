t = int(input())

for _ in range(t):
    line = input()
    line = [int(i) for i in line]
    n = len(line)

    print(line[0], end="")
    i = 1
    while i < n and line[i - 1] <= line[i] and i < n:
        print(line[i], end="")
        i += 1
    while i < n and line[i - 1] >= line[i] and i < n:
        print(line[i], end="")
        i += 1
    c = i - 1
    while i < n:
        print(line[c], end="")
        i += 1
    print()

