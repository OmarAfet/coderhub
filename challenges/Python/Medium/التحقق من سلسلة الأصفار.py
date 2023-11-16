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