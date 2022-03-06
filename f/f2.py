def input_args(convert_int: bool = True):
    line = input().split()
    if convert_int:
        line = [int(i) for i in line]
    return line

def input_n(n: int):
    res = []
    for _ in range(n):
        line = input_args()
        res.append(line[0])
    return res

def rise(n: int) -> int:
    i = 0
    prev = -1
    inc = True
    inc_begin = 0
    dec_begin = None
    n_copy = n
    while n:
        cur = n%10
        n = n//10
        if inc:
            if prev > cur:
                inc = False
                dec_begin = i-1
        else:
            if prev < cur:
                inc = True
                inc_begin = i-1
        prev = cur
        i += 1
    if dec_begin is not None:
        if dec_begin != 0:
            fall_digit = get_digit(n_copy, inc_begin)
            # print(fall_digit, inc_begin)
            fall_tail = 0
            for i in range(inc_begin):
                fall_tail *= 10
                fall_tail += fall_digit
        else:
            fall_tail = 0

    else:
        return n_copy
    # print(inc_begin, dec_begin)
    rise = (n_copy // 10 ** inc_begin) * 10**inc_begin
    # fall = (n_copy // 10 ** dec_begin) * 10**dec_begin
    # fall = fall % 10**(inc_begin-dec_begin) * 10**dec_begin
    # print(rise, fall, fall_tail)
    return rise+fall_tail


def get_digit(number, n):
    # print(number, n)
    return number // 10**n % 10

n = input_args()[0]
data = input_n(n)
for i in data:
    print(rise(i))