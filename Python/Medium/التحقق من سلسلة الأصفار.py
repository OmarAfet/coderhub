
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def longestZero(strParam: str) -> str:
    longest = 0
    new_longest = 0
    for i in strParam:
        if i == "0":
            new_longest += 1
        else:
            longest = max(longest, new_longest)
            new_longest = 0
    
    result = ""
    for i in range(max(longest, new_longest)):
        result += "0"
    
    return result