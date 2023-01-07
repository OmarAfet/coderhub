
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def similarOrdered(word1: str, word2: str) -> str:
    sorted_words = sorted([word1, word2])
    sorted_words = [''.join(sorted(set(word))) for word in sorted_words]
    longest_substring = ''
    for i in range(len(sorted_words[0])):
        for j in range(i+1, len(sorted_words[0])+1):
            substring = sorted_words[0][i:j]
            if substring in sorted_words[1] and len(substring) > len(longest_substring):
                longest_substring = substring
    if longest_substring:
        return longest_substring
    else:
        return "No matches found"