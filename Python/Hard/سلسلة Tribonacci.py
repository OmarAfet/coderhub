
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def tribonacci(num):
    if num == 0:
        return []
    elif num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    elif num == 3:
        return [1, 1, 1]
    else:
        t = tribonacci(num - 1)
        next_num = t[-1] + t[-2] + t[-3]
        t.append(next_num)
        return t