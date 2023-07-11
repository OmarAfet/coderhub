
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def first_n_vowels(phrase: str, n: int) -> str:
    vowels = 'aeiouAEIOU'
    result = ''
    for ch in phrase:
        if ch in vowels:
            result += ch
    if len(result) < n:
        return
    else:
        return result[:n]