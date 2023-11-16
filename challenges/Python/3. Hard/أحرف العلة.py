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