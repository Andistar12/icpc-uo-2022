s = str(input())

ss = s + s

sr = "".join(list(reversed(s)))

if sr in ss:
    print("1")
else:
    print("0")
