
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

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