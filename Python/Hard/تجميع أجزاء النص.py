
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def isInterleave(A: str, B: str, C: str) -> bool:
    for i in A:
        if i in C:
            C = C.replace(i, "", 1)
        else:
            return False

    for i in B:
        if i in C:
            C = C.replace(i, "", 1)
        else:
            return False
        
    return True